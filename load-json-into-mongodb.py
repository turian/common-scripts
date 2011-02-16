#!/usr/bin/python
"""
Load JSON from stdin into a MongoDB

USAGE:
    ./load-json-into-mongodb.py -c collectionname
"""

import sys, string
import common.mongodb
import common.json

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="database name")
parser.add_option("-p", "--port", dest="port", help="port number for mongodb", type="int")
parser.add_option("--hostname", dest="hostname", help="hostname for mongodb")
(options, args) = parser.parse_args()

collection = common.mongodb.collection(DATABASE=options.database, name=options.collection, PORT=options.port, HOSTNAME=options.hostname)
print "%s starts with %d docs" % (collection, collection.count())

print "Reading JSON from sys.stdin..."
docs = common.json.load(sys.stdin)
print "Read %d docs from sys.stdin JSON..." % len(docs)
assert len(docs)>0

for doc in docs:
    doc["_id"] = doc["IncidentId"]
    collection.save(doc)
print "%s now has %d docs" % (collection, collection.count())
