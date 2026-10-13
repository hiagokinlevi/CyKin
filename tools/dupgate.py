#!/usr/bin/env python3
"""Manuscript duplicate gate.

Usage: python3 tools/dupgate.py [BASE_REF]   (default: origin/main)

For every levels/**/MANUSCRIPT.md changed between the merge base of HEAD and
BASE_REF, count near-duplicate sentence pairs inside each numbered section
(### N.M headings). Two sentences of at least five words are near-duplicates
when the Jaccard similarity of their word sets is above 0.6. Fenced code and
the worked-results appendix are ignored.

The gate fails (exit 1) only when a manuscript has MORE pairs than its version
on the base ref. Existing debt is tolerated; new manuscripts must have zero.
This blocks "top-up" edits that restate a section's lead paragraph to reach a
word-count floor.
"""
import re
import subprocess
import sys

THRESHOLD = 0.6
MIN_WORDS = 5
SECTION_RE = re.compile(r'^### (\d+\.\d+ [^\n]*)\n(.*?)(?=^#{2,3} |^<a id|\Z)', re.S | re.M)


def words(sentence):
    return set(re.findall(r"[\w']+", sentence.lower()))


def pairs(text):
    text = text.split('<a id="worked-results"></a>')[0]
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    found = []
    for heading, body in SECTION_RE.findall(text):
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', body) if len(s.split()) >= MIN_WORDS]
        for i in range(len(sents)):
            for j in range(i + 1, len(sents)):
                a, b = words(sents[i]), words(sents[j])
                if a | b and len(a & b) / len(a | b) > THRESHOLD:
                    found.append((heading.split()[0], sents[j][:100]))
    return found


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else 'origin/main'
    mb = git('merge-base', 'HEAD', base).stdout.strip() or base
    files = [f for f in git('diff', '--name-only', mb).stdout.split()
             if f.startswith('levels/') and f.endswith('MANUSCRIPT.md')]
    failed = 0
    for f in files:
        try:
            new = pairs(open(f, encoding='utf-8').read())
        except FileNotFoundError:
            continue
        old = git('show', f'{mb}:{f}')
        old = pairs(old.stdout) if old.returncode == 0 else []
        status = 'FAIL' if len(new) > len(old) else 'ok'
        print(f'{status} {f}: {len(old)} -> {len(new)} near-duplicate pairs')
        if len(new) > len(old):
            failed += 1
            for sec, s in new[:10]:
                print(f'    {sec} {s}')
    print(f"dupgate {'fail' if failed else 'pass'}: {len(files)} manuscripts checked, {failed} failed")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
