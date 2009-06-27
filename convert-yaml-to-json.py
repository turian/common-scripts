#!/usr/bin/python
#
#  Convert yaml in sys.stdin to json.
#

import sys
import yaml
from yaml import load, load_all, dump
try:
    from yaml import CLoader as Loader
    from yaml import CDumper as Dumper
    sys.stderr.write("Sweet. Using C yaml...\n")
except ImportError:
    from yaml import Loader, Dumper
    sys.stderr.write("WARNING: Could not use C yaml\n")

import common.file
import common.json

from common.stats import stats

cnt = 0
print "["
for d in load_all(sys.stdin, Loader=Loader):
    if cnt > 0: sys.stdout.write(",\n")
    sys.stdout.write(common.json.dumps(d, indent=4, sort_keys=True))
    cnt += 1
    sys.stderr.write("%d pages loaded...\n" % cnt)
    sys.stderr.write(stats() + "\n")
sys.stderr.write("\n]\n")
