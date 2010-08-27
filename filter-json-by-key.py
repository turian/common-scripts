#!/usr/bin/env python
"""
Filter JSON in sys.stdin to find only keys that are given as arguments.
"""

import sys
assert len(sys.argv) > 1

import common.json
from common.str import percent

keptdocs = []
alldocs = common.json.load(sys.stdin)
for doc in alldocs:
    newdoc = {}
    for k in doc.keys():
        if k in sys.argv[1:]:
            newdoc[k] = doc[k]
    keptdocs.append(newdoc)

common.json.dump(keptdocs, sys.stdout, indent=4)
