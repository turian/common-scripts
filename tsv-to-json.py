#!/usr/bin/python
"""
Read TSV from stdin and output as JSON.
"""

import sys
import string
import common.json

titles = [string.strip(t) for t in string.split(sys.stdin.readline(), sep="\t")]
for l in sys.stdin:
    d = {}
    for t, f in zip(titles, string.split(l, sep="\t")):
        d[t] = f
    print common.json.dumps(d, indent=4)
