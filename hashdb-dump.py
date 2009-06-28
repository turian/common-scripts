#!/usr/bin/python
#
#  Read the Tokyo Cabinet hash database in infile.
#  For each item, print the key and value (pretty-print as YAML).
#  Each value is assumed to be JSON.
#

import sys
import common.myyaml
import common.file
import common.json
from common.stats import stats
import os.path

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile", help="TokyoCabinet infile")
(options, args) = parser.parse_args()
assert options.infile is not None

from common.hashdb import read

sys.stderr.write(stats() + "\n")
# traverse records
for (key, value) in common.hashdb.read(options.infile):
    sys.stderr.write(stats() + "\n")
    print key
    print common.myyaml.dump(value)
#    if key in value:
#        print value
#    else:
#        print key, value
sys.stderr.write(stats() + "\n")
