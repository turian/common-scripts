#!/usr/bin/python
"""
Count the number of entries in a mongodb collection.

USAGE:
    ./mongodb-count.py -d databasename -c collectionname
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

assert options.database is not None
assert options.collection is not None
collection = common.mongodb.collection(DATABASE=options.database, name=options.collection, PORT=options.port, HOSTNAME=options.hostname)
print collection.count()
