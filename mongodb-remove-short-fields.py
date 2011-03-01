#!/usr/bin/python
"""
Remove every occurrence of some field if it is shorter than some length,
for every row, in MongoDB
"""

import sys, string
import common.mongodb
import common.json
import common.str

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="database name")
parser.add_option("-f", "--field", dest="field", help="field name")
parser.add_option("-l", "--minlength", dest="minlength", help="minimum length to keep the field.", type="int")
parser.add_option("-p", "--port", dest="port", help="port number for mongodb", type="int")
parser.add_option("--hostname", dest="hostname", help="hostname for mongodb")
(options, args) = parser.parse_args()

assert options.field is not None
assert options.minlength is not None

collection = common.mongodb.collection(DATABASE=options.database, name=options.collection, PORT=options.port, HOSTNAME=options.hostname)
cnt = 0
tot = 0
for doc in common.mongodb.findall(collection, matchfn=lambda doc: options.field in doc, matchfn_description="has field %s" % options.field):
    tot += 1
    if len(doc[options.field]) >= options.minlength: continue
    cnt += 1
    print "FAKING IT, not actually removing %s: %s" % (options.field, repr(doc[options.field]))
#    del doc[options.field]
#    collection.save(doc)

print >> sys.stderr, "Removed %s docs that are too short" % (common.str.percent(cnt, tot))
