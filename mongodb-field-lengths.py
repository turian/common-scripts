#!/usr/bin/python
"""
Print MongoDB field length and field, for every row.
"""

import sys, string
import common.mongodb
import common.json

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="database name")
parser.add_option("-f", "--field", dest="field", help="field name")
parser.add_option("-p", "--port", dest="port", help="port number for mongodb", type="int")
parser.add_option("--hostname", dest="hostname", help="hostname for mongodb")
(options, args) = parser.parse_args()

assert options.field is not None

collection = common.mongodb.collection(DATABASE=options.database, name=options.collection, PORT=options.port, HOSTNAME=options.hostname)
for doc in common.mongodb.findall(collection, matchfn=lambda doc: options.field in doc, matchfn_description="has field %s" % options.field):
    print len(doc[options.field]), repr(doc[options.field])[:1000]
