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
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as mardown:
        with open(sys.argv[2], 'w', encoding='utf-8') as output:
            for line in mardown.readlines():
                nbr = line.count("#")
                output.write(f"<h{nbr}>{line[nbr:].strip()}</h{nbr}>\n")

    # Nothing went wrong
    exit(0)
