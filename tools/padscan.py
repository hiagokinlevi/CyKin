#!/usr/bin/env python3
"""Restating-padding detector for CyberABC manuscripts.

Signals per numbered section (### N.M ...):
  SENT  sentence whose TF-IDF cosine to an earlier sentence of the same section is >= --sent (0.45)
        and that adds <= --novel (2) content words not already said in the section (restatement)
  PARA  consecutive prose paragraphs with TF-IDF cosine >= --para (default 0.35)
  LEAD  opening paragraph whose sentences each restate a bullet of the list that follows
        (>= 60% of its sentences have cosine >= --lead to some bullet)
  CLOSE 'Closing note'/'In short'/'To sum up' paragraph with cosine >= --para to the rest of the section
  WEX   short trailing example (unnumbered '### Worked example'/'Example'/'Exemplo resolvido'/'Ejemplo resuelto'
        heading inside a numbered section, prose body <= --wexmax (80) words) whose content words are mostly
        already in the section before it: novel-token share <= --wexnov (0.25). Tuned on #1406/#1413/#1420/#1431.
        --wexdebug prints cos/novelty for every short example.
  COPY  sentence (>= 12 words) appearing verbatim (normalized) in another section or book
  HEAD  placeholder heading (Bit2, Story, 3.q10, x.x, TODO) or doubled number ('3.9 3.x')
TF-IDF: lowercase word tokens, stopwords removed, crude suffix stemming, IDF over the book's sections.
Usage: padscan.py [--lang en] [--rank] [--show] [paths...]   (default: every levels/*/*/<lang>/book/MANUSCRIPT.md)
"""
import re, sys, math, glob, argparse, collections
SW=set("""a an the and or but if then than that this these those of to in on at by for with from as is are was were be been being it its
into not no do does did so such can could should would will may might must has have had their they them there here which who whom what when
where why how each every any all one two our we you your he she his her also only more most other same before after over under about up out
""".split())
def stem(w):
    for s in ('ations','ation','ings','ing','edly','ed','ies','es','s','ly'):
        if len(w)>len(s)+3 and w.endswith(s): return w[:-len(s)]
    return w
def toks(t):
    t=re.sub(r'`[^`]*`|\[[^\]]*\]\([^)]*\)|https?://\S+','',t)
    return [stem(w) for w in re.findall(r"[a-zà-ÿ0-9]+",t.lower()) if w not in SW and len(w)>2]
def sents(t): return [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"(])',t.strip()) if len(s.split())>=4]
HEADRX=[('placeholder',re.compile(r'^#{2,4}\s+(?:\d+(?:\.\d+)*\s+)?(Bit\s*\d+|Story|Scene|Extra|Pad|Extension|Part\s*\d+|Section\s*\d*|TODO|TBD|x+)\s*$',re.I)),
        ('qcode',re.compile(r'^#{2,4}\s+\d+\.q\d+\b',re.I)),
        ('doubled',re.compile(r'^#{2,4}\s+\d+\.\d+\s+\d+\.(?:\d+|x)\b',re.I)),
        ('xnum',re.compile(r'^#{2,4}\s+\d+\.x\b',re.I))]
def parse(path):
    secs=[];cur=None;block=[];code=False;heads=[]
    def flush():
        if block and cur is not None:
            txt=' '.join(l.strip() for l in block)
            kind='list' if re.match(r'\s*([-*+]|\d+[.)])\s',block[0]) else 'table' if block[0].lstrip().startswith('|') else 'quote' if block[0].lstrip().startswith('>') else 'para'
            if kind=='list':
                items=[];
                for l in block:
                    if re.match(r'\s*([-*+]|\d+[.)])\s',l): items.append(re.sub(r'^\s*([-*+]|\d+[.)])\s+','',l))
                    elif items: items[-1]+=' '+l.strip()
                cur['blocks'].append(('list',items))
            else: cur['blocks'].append((kind,txt))
        block.clear()
    for i,l in enumerate(open(path,encoding='utf-8'),1):
        l=l.rstrip('\n')
        if l.startswith('```'): flush(); code=not code; continue
        if code: continue
        if re.match(r'^#{1,6}\s',l):
            flush()
            for k,rx in HEADRX:
                if rx.match(l): heads.append((i,k,l))
            m=re.match(r'^#{3,4}\s+(\d+\.\d+)\b\s*(.*)',l)
            if m: cur={'id':m.group(1),'title':m.group(2),'line':i,'blocks':[]}; secs.append(cur)
            elif l.startswith('## '): cur=None
            elif cur is not None: cur['blocks'].append(('head',l))
            continue
        if not l.strip() or l.strip().startswith('<'): flush(); continue
        if block and re.match(r'\s*([-*+]|\d+[.)])\s',l) and not re.match(r'\s*([-*+]|\d+[.)])\s',block[0]): flush()
        block.append(l)
    flush(); return secs,heads
class TFIDF:
    def __init__(s,docs):
        s.N=len(docs) or 1; s.df=collections.Counter()
        for d in docs: s.df.update(set(toks(d)))
    def vec(s,t):
        c=collections.Counter(toks(t)); v={w:(1+math.log(n))*math.log((s.N+1)/(s.df[w]+1)+1) for w,n in c.items()}
        z=math.sqrt(sum(x*x for x in v.values())) or 1; return {w:x/z for w,x in v.items()}
    @staticmethod
    def cos(a,b): return sum(x*b.get(w,0) for w,x in a.items())
CLOSERX=re.compile(r'^(\*\*)?(closing note|in short|to sum up|in summary|the point is|put simply|in other words|overall)',re.I)
WEXRX=re.compile(r'^#{3,5}\s+(worked example|example|exemplo resolvido|exemplo|ejemplo resuelto|ejemplo)\b',re.I)
def norm(s): return ' '.join(re.findall(r'[a-z0-9]+',s.lower()))
def scan(path,a,copyidx):
    secs,heads=parse(path); out=[]
    words=sum(len(t.split()) if k!='list' else sum(len(x.split()) for x in t) for s in secs for k,t in s['blocks'] if k!='head')
    tf=TFIDF([' '.join(t if k!='list' else ' '.join(t) for k,t in s['blocks'] if k!='head') for s in secs])
    for s in secs:
        B=s['blocks']; paras=[(i,t) for i,(k,t) in enumerate(B) if k=='para']
        for (i,x),(j,y) in zip(paras,paras[1:]):
            if j==i+1 and len(x.split())>=15 and len(y.split())>=15:
                c=tf.cos(tf.vec(x),tf.vec(y))
                if c>=a.para: out.append(('PARA',s,round(c,2),y[:110]))
        seen=[];seenw=set()
        for k,t in B:
            if k in ('table','head'): continue
            for x in (sents(t) if k!='list' else t):
                if re.match(r'\W*EX\d+',x): continue
                tx=set(toks(x)); vx=tf.vec(x)
                if len(tx)>=5 and seen:
                    c=max(tf.cos(vx,v) for v in seen); nov=len(tx-seenw)
                    if c>=a.sent and nov<=a.novel: out.append(('SENT',s,f"{c:.2f}/n{nov}",x[:110]))
                seen.append(vx); seenw|=tx
        for i,(k,t) in enumerate(B[:-1]):
            if k=='para' and B[i+1][0]=='list' and len(B[i+1][1])>=2:
                ss=sents(t); iv=[tf.vec(it) for it in B[i+1][1]]
                if len(ss)>=2:
                    hit=sum(1 for x in ss if max(tf.cos(tf.vec(x),v) for v in iv)>=a.lead)
                    if hit/len(ss)>=0.6: out.append(('LEAD',s,round(hit/len(ss),2),t[:110]))
        for idx,(k,t) in enumerate(B):
            if k=='para' and CLOSERX.match(t) and idx>0:
                rest=' '.join(x if kk!='list' else ' '.join(x) for kk,x in B[:idx] if kk!='head')
                c=tf.cos(tf.vec(t),tf.vec(rest))
                if c>=a.para: out.append(('CLOSE',s,round(c,2),t[:110]))
        for h,(k,t) in enumerate(B):
            if k!='head' or not WEXRX.match(t): continue
            body=[];
            for kk,x in B[h+1:]:
                if kk!='para': break
                body.append(x)
            ex=' '.join(body); nw=len(ex.split())
            if not ex or nw>a.wexmax: continue
            before=' '.join(x if kk!='list' else ' '.join(x) for kk,x in B[:h] if kk not in ('head','table'))
            tx=set(toks(ex)); 
            if len(tx)<3: continue
            nov=len(tx-set(toks(before)))/len(tx); c=tf.cos(tf.vec(ex),tf.vec(before))
            if a.wexdebug: print(f"WEXDBG {path.split('/')[1][:5]}/{path.split('/')[2][:12]} {s['id']} cos={c:.2f} nov={nov:.2f} w={nw} {ex[:90]}")
            if nov<=a.wexnov: out.append(('WEX',s,f"{c:.2f}/n{nov:.2f}",ex[:110]))
        if copyidx is not None:
            for k,t in B:
                for x in (sents(t) if k!='list' else t):
                    if '](' in x or x.lstrip().startswith(('**EX','EX')): continue
                    n=norm(x)
                    if len(n.split())>=12 and len({o[0] for o in copyidx.get(n,())})<=a.boiler and len(copyidx.get(n,()))>1:
                        others=[o for o in copyidx[n] if o!=(path,s['id'])]
                        if others: out.append(('COPY',s,len(others),x[:110]+' || '+'; '.join(f"{o[0].split('/')[2][:14]}/{o[0].split('/')[1][:5]} {o[1]}" for o in others[:3])))
    for i,k,l in heads: out.append(('HEAD',{'id':'L%d'%i,'title':'','line':i},k,l))
    return out,words
def main():
    p=argparse.ArgumentParser(); p.add_argument('paths',nargs='*'); p.add_argument('--lang',default='en')
    p.add_argument('--para',type=float,default=0.35); p.add_argument('--lead',type=float,default=0.35)
    p.add_argument('--sent',type=float,default=0.45); p.add_argument('--novel',type=int,default=2); p.add_argument('--rank',action='store_true'); p.add_argument('--show',action='store_true'); p.add_argument('--nocopy',action='store_true'); p.add_argument('--wexmax',type=int,default=80); p.add_argument('--wexnov',type=float,default=0.25); p.add_argument('--wexdebug',action='store_true'); p.add_argument('--boiler',type=int,default=4,help='ignore sentences shared by more than N books (course template)')
    a=p.parse_args(); paths=a.paths or sorted(glob.glob(f'levels/*/*/{a.lang}/book/MANUSCRIPT.md'))
    copyidx=None
    if not a.nocopy:
        copyidx=collections.defaultdict(set)
        for f in sorted(glob.glob(f'levels/*/*/{a.lang}/book/MANUSCRIPT.md')):
            for s in parse(f)[0]:
                for k,t in s['blocks']:
                    if k in('para','list'):
                        for x in (sents(t) if k=='para' else t): copyidx[norm(x)].add((f,s['id']))
    rows=[]
    for f in paths:
        out,w=scan(f,a,copyidx); c=collections.Counter(o[0] for o in out)
        secsf=len({o[1]['id'] for o in out if o[0]!='HEAD'})
        sc=sum({'PARA':0.5,'HEAD':2}.get(o[0],1) for o in out); rows.append((round(1e4*sc/max(w,1),1),f,w,c,secsf))
        if a.show:
            for kind,s,v,t in out: print(f"{kind:5} {s['id']:>6} L{s['line']:<5} {v}  {t}")
    if a.rank or not a.show:
        for score,f,w,c,n in sorted(rows,reverse=True):
            print(f"{score:6} per10k  secs={n:3} {' '.join(f'{k}={c[k]}' for k in ('SENT','PARA','LEAD','CLOSE','WEX','COPY','HEAD'))}  {f.split('/')[1]}/{f.split('/')[2]}  ({w}w)")
    sys.exit(0)
if __name__=='__main__': main()
