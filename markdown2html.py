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
        mkd_lines = mardown.readlines()
        l_nbr = len(mkd_lines)

    with open(sys.argv[2], 'w', encoding='utf-8') as output:
        for idx in range(l_nbr):
            nbr = mkd_lines[idx].count("#")
            output.write(f"<h{nbr}>{mkd_lines[idx][nbr:].strip()}</h{nbr}>")
            if idx+1 != l_nbr:
                output.write('\n')

    # Nothing went wrong
    exit(0)
