#!/usr/bin/env python
"""
Read all mongo docs, and insert them into Lucene.
"""

import common.lucene
import common.mongodb
import sys, os, lucene

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--storefield", dest="storefield", help="fields to store in Lucene (store, don't index)", type="string", action="append")
parser.add_option("-i", "--contentfield", dest="contentfield", help="content field in Lucene (index, don't store)", type="string")
parser.add_option("-l", "--lucenedir", dest="lucenedir", help="directory to store Lucene", type="string")
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="database name")
parser.add_option("-p", "--port", dest="port", help="port number for mongodb", type="int")
parser.add_option("--hostname", dest="hostname", help="hostname for mongodb")
(options, args) = parser.parse_args()

print options.storefield
collection = common.mongodb.collection(DATABASE=options.database, name=options.collection, PORT=options.port, HOSTNAME=options.hostname)
print dir(common.lucene)
common.lucene.from_mongodb(collection, options.storefield, options.contentfield, options.lucenedir)

lucene.initVM(lucene.CLASSPATH)
print 'lucene', lucene.VERSION

