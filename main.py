"""food-picture-01 entry v2: spicy tantanmen noodle pull with iced ocha.

The program ships one picture (entry.png) and copies it byte-for-byte to
the output directory. Copying is deterministic: the same input bytes always
produce the same output bytes. After copying, it checks the output size
matches the source so a truncated write can never pass silently.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
