#!/usr/bin/python
"""
Dump the MongoDB

USAGE:
    ./dumpdb.py -c collectionname
"""

import sys, string
import common.mongodb
import common.json

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="databse name")
(options, args) = parser.parse_args()

collection = common.mongodb.collection(DATABASE=options.database, name=options.collection)
for doc in common.mongodb.findall(collection, matchfn=lambda doc: True):
    common.json.dump(doc, sys.stdout, indent=4)
#    print string.strip(doc["content"].encode("utf-8"))
