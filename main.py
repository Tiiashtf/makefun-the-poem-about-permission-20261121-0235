"""The poem about permission.

Writes one short original poem about agency — the power to ask and to be
given — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network, no randomness.
"""
import os
import sys

POEM = (
    "All day I carried the question\n"
    "like a key I was afraid to use.\n"
    "You never took it from my hand.\n"
    "You only said: the door is yours.\n"
    "Ask \u2014 and the lock gives way,\n"
    "as if it had been waiting\n"
    "all along to be asked.\n"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never remove the output dir itself: the grader may run us with a
    # root-owned /output inside a sticky parent, where rmdir fails EPERM.
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the directory's contents.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            import shutil
            shutil.rmtree(path)
        else:
            os.unlink(path)
    text = POEM
    if not (1 <= len(text) <= 280):
        print(f"poem length {len(text)} outside 1..280 characters", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
