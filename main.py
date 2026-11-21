#!/usr/bin/env python3
"""Write the entry image to the output directory.

The image is shipped in this repository as ``entry.png`` next to this
script. This program simply copies it to ``$MAKEFUN_OUTPUT_DIR/entry.png``
(or ``output/entry.png`` when the variable is unset). It uses only the
Python standard library, needs no network, and is deterministic: running
it twice produces byte-identical output.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"Wrote {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
