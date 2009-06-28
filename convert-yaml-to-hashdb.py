#!/usr/bin/python
#
#  Read the list of items in the YAML infile.
#  For each items, find the key. Add this to a Tokyo Cabinet hash database
#  (outfile), with the value the JSON encoding of the item.
#
#  Usage: convert-yaml-to-hashdb.py [options]
#  Options:
#   -h, --help            show this help message and exit
#   -i INFILE, --infile=INFILE
#                         YAML input file, a list
#   -o OUTFILE, --outfile=OUTFILE
#                         Tokyo Cabinet outfile
#   -k KEY, --key=KEY     Name of key in YAML input
#

import sys
import common.myyaml
import common.file
import common.json
from common.stats import stats
import os.path

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile", help="YAML input file, a list")
parser.add_option("-o", "--outfile", dest="outfile", help="Tokyo Cabinet outfile")
parser.add_option("-k", "--key", dest="key", help="Name of key in YAML input")
(options, args) = parser.parse_args()
assert options.infile is not None
assert options.outfile is not None
assert options.key is not None

from common.hashdb import create
hdb = common.hashdb.create(options.outfile)

cnt = 0
for d in common.myyaml.load_all(common.file.myopen(options.infile)):
    hdb.put(d[options.key], common.json.dumps(d, indent=4, sort_keys=True))
    cnt += 1
    if cnt % 10 == 0:
        sys.stderr.write("%d items loaded...\n" % cnt)
        sys.stderr.write(stats() + "\n")
hdb.close()
