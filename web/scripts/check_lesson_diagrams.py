"""Reject repetitive, automatically inserted lesson-navigation diagrams.

Content-specific diagrams remain welcome; this check only catches the old
generated figure blocks and their generic lesson-map headings.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
GENERIC_HEADING = re.compile(
    r"^#{3,5} (?:Lesson map|Mapa da aula|Mapa de la lección|"
    r"Logical drawing|Desenho lógico|Dibujo lógico)\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def main() -> int:
    failures = []
    for path in ROOT.glob("levels/**/book/MANUSCRIPT.md"):
        source = path.read_text(encoding="utf-8")
        if "lesson-figures:" in source or GENERIC_HEADING.search(source):
            failures.append(path.relative_to(ROOT))
    if failures:
        print(f"Found generic lesson-navigation diagrams in {len(failures)} manuscripts:")
        for path in failures[:20]:
            print(f"  {path}")
        if len(failures) > 20:
            print(f"  ... and {len(failures) - 20} more")
        return 1
    print("No generic lesson-navigation diagrams in public manuscripts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
