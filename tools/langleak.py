#!/usr/bin/env python3
"""Untranslated-English leak detector for PT/ES book manuscripts.

Usage:
  python3 tools/langleak.py [--lang pt|es|all] [--summary] [FILE ...]
  python3 tools/langleak.py --gate [BASE_REF]   # changed PT/ES manuscripts vs base

Prose only: fenced code, inline code, URLs, link targets, HTML anchors, IDs
(EX001, CVE-..., ABC-12), quoted titles ("..." and *...*), reference-list
entries (lines with a year, under Referências/Referencias/Bibliografia
headings) and table rows made only of code are ignored.

A line is flagged when either
  F: a window of 8 words holds >= 3 English function words (the, and, which...)
  V: >= 3 consecutive words (commas allowed) are "English-only" vocabulary:
     words frequent in all EN manuscripts but nearly absent from PT/ES prose.
Gate mode fails when a changed manuscript has more flags than on BASE_REF.
"""
import glob, os, re, subprocess, sys
from collections import Counter

FUNC = set("""the and but which with that is are was were of to for this these
those from by be been being not or it its an have has had will would can could
should into than then there their they them what when where who whose while
also only such each other more most any all our your we you he she his her
on at as if so do does did no yes about after before over under between""".split())
# words that are also PT/ES words or common loanwords
FUNC -= {"a", "e", "do", "no", "as", "so", "on"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORD = re.compile(r"[A-Za-zÀ-ÿ'][A-Za-zÀ-ÿ'-]*")
# accepted English technical terms (kept in English in PT/ES by convention)
ALLOW = ['content security policy', 'trust services criteria', 'harvest now, decrypt later',
         'harvest now decrypt later', 'fast gradient sign method', 'request link status',
         'unable to get local issuer certificate', 'usable security', 'access review',
         'unconfirmed user data', 'confirmed user data',
         # STRIDE threat categories (kept in English with a gloss, as in EN/PT)
         'spoofing identity', 'tampering with data', 'repudiation',
         'information disclosure', 'denial of service', 'elevation of privilege']
REFHEAD = re.compile(r'^#+ .*(Refer[eê]ncias|Bibliograf|References|Fontes|Fuentes|Leituras|Lecturas)', re.I)


def prose_lines(text):
    out, code, ref = [], False, False
    for i, ln in enumerate(text.split('\n'), 1):
        s = ln.strip()
        if s.startswith('```') or s.startswith('~~~'):
            code = not code; continue
        if code or ln.startswith('    ') or s.startswith('<'):
            continue
        if s.startswith('#'):
            ref = bool(REFHEAD.match(s))
        if ref and s and not s.startswith('#'):
            continue
        if re.search(r'\b(19|20)\d\d[a-z]?\b', s) and re.search(r'\(\d{4}\)|\d{4}\.|et al|doi|ISBN|https?:', s):
            continue  # reference-like entry
        if re.match(r'- [^*]*\[[^\]]+\]', s) and '**' not in s:
            continue  # reference entry: - Author. [Title](url)
        for t in ALLOW:
            s = re.sub(re.escape(t), ' | ', s, flags=re.I)
        s = re.sub(r'`[^`]*`', ' ', s)
        s = re.sub(r'\]\([^)]*\)', ']', s)
        s = re.sub(r'"[^"]*"|“[^”]*”|«[^»]*»', ' | ', s)
        s = re.sub(r'\[[^\]]*\]', ' | ', s)          # link text / reference titles
        s = re.sub(r'\*\*[^*]+\*\*', ' | ', s)        # bold terms (often EN UI labels)
        s = re.sub(r'\([^()]*\)', ' | ', s)          # parenthetical glosses
        s = re.sub(r'\{[^}]*\}|\S*_\S*', ' | ', s)    # schemas, identifiers
        s = re.sub(r'https?://\S+', ' ', s)
        s = re.sub(r'(?<!\*)\*[^*\n]+\*(?!\*)', ' | ', s)
        s = re.sub(r'\b[A-Z]{2,}[-_]?\d+[\w.-]*', ' ', s)
        out.append((i, s))
    return out


def tokens(s):
    # keep commas as joiners, other punctuation breaks runs
    return re.findall(r"[A-Za-zÀ-ÿ'][A-Za-zÀ-ÿ'-]*|,|[^\sA-Za-zÀ-ÿ',]+", s)


_VOCAB = {}
RATIO = float(os.environ.get('LANGLEAK_RATIO', '0.3'))


def english_only(lang):
    if lang in _VOCAB:
        return _VOCAB[lang]
    en, other = Counter(), Counter()
    for p in glob.glob(f'{ROOT}/levels/*/*/en/book/MANUSCRIPT.md'):
        for _, s in prose_lines(open(p).read()):
            en.update(w.lower() for w in WORD.findall(s))
    for p in glob.glob(f'{ROOT}/levels/*/*/{lang}/book/MANUSCRIPT.md'):
        for _, s in prose_lines(open(p).read()):
            other.update(w.lower() for w in WORD.findall(s))
    ten, tot = sum(en.values()) or 1, sum(other.values()) or 1
    v = {w for w, c in en.items() if c >= 3 and len(w) > 2 and other[w] / tot < RATIO * c / ten}
    _VOCAB[lang] = v
    return v


def scan_text(text, lang):
    vocab = english_only(lang) | FUNC
    hits = []
    for i, s in prose_lines(text):
        toks = tokens(s)
        words = [t for t in toks if WORD.fullmatch(t) and not t.isupper()]
        f = any(sum(w.lower() in FUNC for w in words[k:k + 8]) >= 3 for k in range(max(1, len(words) - 7)))
        run, best, cur, span = 0, 0, [], ''
        for t in toks + ['.']:
            if t == ',':
                cur.append(t); continue
            if WORD.fullmatch(t) and t.lower() in vocab and not t[0].isupper():
                run += 1; cur.append(t)
            else:
                if run > best:
                    best, span = run, ' '.join(cur)
                run, cur = 0, []
        v = best >= 3
        if f and not span:
            k = max(range(max(1, len(words) - 7)), key=lambda k: sum(w.lower() in FUNC for w in words[k:k + 8]))
            span = ' '.join(words[k:k + 8])
        if f or v:
            hits.append((i, ('F' if f else '') + ('V' if v else ''), span.replace(' ,', ',')))
    return hits


def lang_of(path):
    return 'es' if '/es/' in path else 'pt'


def gate(base):
    mb = subprocess.run(['git', 'merge-base', 'HEAD', base], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    files = subprocess.run(['git', 'diff', '--name-only', mb], capture_output=True, text=True, cwd=ROOT).stdout.split()
    bad = 0
    for f in files:
        if not re.match(r'levels/.*/(pt|es)/book/MANUSCRIPT\.md$', f) or not os.path.exists(f'{ROOT}/{f}'):
            continue
        new = len(scan_text(open(f'{ROOT}/{f}').read(), lang_of(f)))
        old_t = subprocess.run(['git', 'show', f'{mb}:{f}'], capture_output=True, text=True, cwd=ROOT)
        old = len(scan_text(old_t.stdout, lang_of(f))) if old_t.returncode == 0 else 0
        st = 'FAIL' if new > old else 'ok'
        print(f'langleak {st} {f} {old}->{new}')
        bad += new > old
    return 1 if bad else 0


def main(a):
    if '--gate' in a:
        rest = [x for x in a if x != '--gate']
        sys.exit(gate(rest[0] if rest else 'origin/main'))
    lang = 'all'
    if '--lang' in a:
        lang = a[a.index('--lang') + 1]; a = [x for x in a if x not in ('--lang', lang)]
    summary = '--summary' in a
    files = [x for x in a if not x.startswith('--')]
    if not files:
        langs = ['pt', 'es'] if lang == 'all' else [lang]
        files = sorted(p for l in langs for p in glob.glob(f'{ROOT}/levels/*/*/{l}/book/MANUSCRIPT.md'))
    for p in files:
        hits = scan_text(open(p).read(), lang_of(p))
        name = os.path.relpath(p, ROOT)
        if summary:
            if hits: print(len(hits), name)
        else:
            for i, k, s in hits:
                print(f'{name}:{i}: [{k}] {s}')


if __name__ == '__main__':
    main(sys.argv[1:])
