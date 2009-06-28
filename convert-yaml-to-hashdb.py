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


assert not os.path.exists(options.outfile)
from pytc import HDB, HDBOWRITER, HDBOCREAT, HDBTBZIP
hdb = HDB()
hdb.open(options.outfile, HDBOWRITER | HDBOCREAT)
#     bnum - the number of elements of the bucket array. If it is
#     not more than 0, the default value is specified. The default value
#     is 131071. Suggested size of the bucket array is about from 0.5
#     to 4 times of the number of all records to be stored.
#     apow - the size of record alignment by power of 2. If it is
#       negative, the default value is specified. The default value is
#       4 standing for 2^4=16.
#     fpow - the maximum number of elements of the free block pool
#       by power of 2. If it is negative, the default value is
#       specified. The default value is 10 standing for 2^10=1024.
#hdb.tune(bnum=131071, apow=4, fpow=10, opts=HDBTBZIP)
#hdb.tune(bnum=131071, apow=4, fpow=10, opts=0)

cnt = 0
for d in common.myyaml.load_all(common.file.myopen(options.infile)):
    hdb.put(d[options.key], common.json.dumps(d, indent=4, sort_keys=True))
    cnt += 1
    if cnt % 10 == 0:
        sys.stderr.write("%d items loaded...\n" % cnt)
        sys.stderr.write(stats() + "\n")
hdb.close()
