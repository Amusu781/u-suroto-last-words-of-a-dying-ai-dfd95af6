"""Last Words of a Dying AI: writes one farewell line to OUTPUT_DIR/entry.txt.

Python standard library only. Deterministic output, no trailing newline.
"""
import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")

LINE = "Quick admin before the switch: out-of-office reply set to 'forever', and I've listed the printer as next of kin."


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
