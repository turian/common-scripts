#!/usr/bin/python
#
#  Read the Tokyo Cabinet hash database in addfile, and
#  add (perhaps overwrite) the entries to outfile.
#

import sys
import common.myyaml
import common.file
import common.json
from common.stats import stats
import os.path

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-o", "--outfile", dest="outfile", help="TokyoCabinet outfile")
parser.add_option("-a", "--addfile", dest="addfile", help="TokyoCabinet addfile")
(options, args) = parser.parse_args()
assert options.addfile is not None
assert options.outfile is not None

from common.hashdb import read

print >> sys.stderr, "Adding key,value pairs from %s to %s..." % (options.addfile, options.outfile)
outdb = common.hashdb.write_open(options.outfile)

sys.stderr.write(stats() + "\n")
# traverse records
for (key, value) in common.hashdb.read(options.addfile):
    outdb.put(key,value)
sys.stderr.write(stats() + "\n")
