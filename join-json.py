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
    docs = common.json.loadfile(f)
    print >> sys.stderr, "Read %d docs from %s..." % (len(docs), f)
    alldocs += docs

print >> sys.stderr, "TOTAL: %d docs" % len(alldocs)
common.json.dump(alldocs, sys.stdout, indent=4)
