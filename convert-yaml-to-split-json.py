#!/usr/bin/python
#
#  Convert yaml in sys.stdin to json.
#  Split into NFILES=10 files, named split%d.json.gz
#

NFILES=10
outfiles = [myopen("split%d.json.gz" % i) for i in range(NFILES)]

import sys
import common.myyaml
import common.file
import common.json

from common.stats import stats

cnt = 0
for o in outfiles:
    o.write("[\n")
for d in common.myyaml.load_all(sys.stdin):
    o = outfiles[cnt % NFILES]
    if cnt >= NFILES: o.write(",\n")
    o.write(common.json.dumps(d, indent=4, sort_keys=True))
    cnt += 1
    sys.stderr.write("%d pages loaded...\n" % cnt)
    sys.stderr.write(stats() + "\n")
for o in outfiles:
    o.write("\n]\n")
    o.close()
