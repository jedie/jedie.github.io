#!/usr/bin/env python3
# encoding: utf-8

import os
from pathlib import Path

import datetime

PICTURE_EXT=(".jpg", ".png")
URL_PREFIX="https://raw.githubusercontent.com/jedie/jedie.github.io/master"

def update_subdir_readme(path):
    path = path.resolve()
    print("Process path: %s" % path)
    for subdir in sorted(path.iterdir()):
        if not subdir.is_dir():
            continue
        print("\n*** %s" % subdir)

        with Path(subdir, "README.creole").open("w") as f:
            for filepath in sorted(subdir.glob('*.*'), reverse=True):
                if filepath.suffix.lower() not in PICTURE_EXT:
                    print(" * SKIP %r: not in PICTURE_EXT, ok." % filepath.name)
                    continue

                content = (
                    "\n== %(name)s ==\n"
                    "{{%(url_prefix)s/%(path)s|%(name)s}}\n"
                ) % {
                    "url_prefix": URL_PREFIX,
                    "path": filepath.relative_to(path.parent),
                    "name": filepath.name
                }
                # print(content)
                f.write(content)

                print(" * %s" % filepath.name)

            content = (
                "\n----\n"
                "(This {{{README.creole}}} was automatic generated with {{{%(filename)s}}} on %(date)s)\n"
            ) % {
                "filename": Path(__file__).name,
                "date": datetime.datetime.utcnow()
            }
            # print(content)
            f.write(content)

def print_dir_links(path):
    path = path.resolve()
    print("\n%s\n" % path)
    for subdir in sorted(path.iterdir()):
        if not subdir.is_dir():
            continue

        content = (
            "* [[%(rel)s|%(name)s]]"
        ) % {
            "rel": subdir.relative_to(path.parent),
            "name": subdir.name
        }
        print(content)

if __name__=="__main__":
    print("Update README files...")
    path=Path("screenshots")

    update_subdir_readme(path)
    print("="*79)
    print_dir_links(path)


