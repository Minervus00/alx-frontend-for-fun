#!/usr/bin/python3
"""This script checks if 2 files are given as argument"""


if __name__ == "__main__":
    import sys
    import os.path

    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr
        )
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}")
        exit(1)

    # Nothing went wrong
    exit(0)
