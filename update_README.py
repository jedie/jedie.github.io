#!/usr/bin/env python3

"""
    Generate READMEs for: https://github.com/jedie/jedie.github.io
"""

import datetime
from pathlib import Path
from urllib.parse import quote


PICTURE_EXT = (".jpg", ".jpeg", ".png")
URL_PREFIX = 'https://raw.githubusercontent.com/jedie/jedie.github.io/main'


def update_subdir_readme(path):
    path = path.resolve()
    print(f"Process path: {path}")
    for subdir in sorted(path.iterdir()):
        if not subdir.is_dir():
            continue
        print(f"\n*** {subdir}")

        with Path(subdir, "README.md").open("w") as f:
            for filepath in sorted(subdir.glob('*.*'), reverse=True):
                if filepath.suffix.lower() not in PICTURE_EXT:
                    print(f" * SKIP {filepath.name!r}: not in PICTURE_EXT, ok.")
                    continue

                f.write(f'\n# {filepath.name}\n\n')

                rel_path = filepath.relative_to(path.parent)
                rel_path_quoted = quote(str(rel_path))

                f.write(f'![{filepath.name}]({URL_PREFIX}/{rel_path_quoted} "{filepath.name}")\n')

                print(f" * {filepath.name}")

            f.write("\n----\n")
            date = datetime.datetime.utcnow()
            f.write(
                f"(This `README.md` was automatic generated with `{Path(__file__).name}` on {date})\n"
            )


if __name__ == "__main__":
    print("Update README files...")
    path = Path("screenshots")

    update_subdir_readme(path)
