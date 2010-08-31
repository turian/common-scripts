#!/usr/bin/env python
"""
For each JSON file in sys.argv, join them and output to stdout.
"""

import sys
assert len(sys.argv) > 1

import common.json
from common.str import percent
alldocs = []
for f in sys.argv[1:]:
    alldocs += common.json.loadfile(f)

common.json.dump(alldocs, sys.stdout, indent=4)
