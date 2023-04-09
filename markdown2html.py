#!/usr/bin/python3
"""This script checks if 2 files are given as argument"""
import sys
import os.path


def write_header():
    # TODO
    pass


def write_unordered():
    # TODO
    pass


if __name__ == "__main__":
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
        # print(mkd_lines)
        l_nbr = len(mkd_lines)

    with open(sys.argv[2], 'w', encoding='utf-8') as output:
        in_unordered = False
        for idx in range(l_nbr):
            # Check unordered list
            if mkd_lines[idx][0] == '-':
                if not in_unordered:
                    in_unordered = True
                    output.write('<ul>\n')

                output.write(f"\t<li>{mkd_lines[idx][1:].strip()}</li>\n")

                # if idx == l_nbr-1 or mkd_lines[idx+1][0] != '\n':
                #     output.write('<ul>\n')
                #     in_unordered = False
                continue

            # Check headers
            nbr = mkd_lines[idx].count("#")
            if nbr != 0:
                if in_unordered:
                    output.write('<ul>\n')
                    in_unordered = False
                output.write(
                    f"<h{nbr}>{mkd_lines[idx][nbr:].strip()}</h{nbr}>\n"
                )
                continue

            # simple line
            if in_unordered and mkd_lines[idx] != '\n':
                output.write('<ul>\n')
                in_unordered = False
            output.write(mkd_lines[idx])

    # Nothing went wrong
    exit(0)
