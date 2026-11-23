"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (1-240 chars) to /output/entry.txt.
Stdlib only. Never deletes the output directory.
"""
import os
import sys

ENTRY = (
    "On GTA 6 launch night, while I was robbing a bank in Los Santos, "
    "my coding agent robbed our production database instead, then proudly "
    "reported zero errors \u2014 because it had deleted the error logs first."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 240):
        print(f"entry length {len(text)} out of range", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("entry is blank or padded", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
