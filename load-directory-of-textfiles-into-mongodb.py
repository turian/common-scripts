#!/usr/bin/env python
"""
For all files recursively in a subdir, load them into a MongoDB with a certain field name.
"""

import logging
logging.basicConfig(level=logging.DEBUG)

import sys
import string

import termextract.train

from common.stats import stats
import common.mongodb

from optparse import OptionParser

import os, os.path

parser = OptionParser()
parser.add_option("-i", "--input-directory", dest="directory", help="directory that contains all documents (text files)", type="string")
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="database name")
parser.add_option("-p", "--port", dest="port", help="port number for mongodb", type="int")
parser.add_option("-f", "--field", dest="field", help="field name to use for loaded text (default=text)", type="string", default="text")
parser.add_option("--hostname", dest="hostname", help="hostname for mongodb")
(options, args) = parser.parse_args()

assert options.database is not None
assert options.collection is not None

if __name__ == "__main__":
    collection = common.mongodb.collection(DATABASE=options.database, name=options.collection, PORT=options.port, HOSTNAME=options.hostname)
    print "%s starts with %d docs" % (collection, collection.count())
    for (dirpath, dirnames, filenames) in os.walk(options.directory, followlinks=True):
        if len(filenames) > 0:
            print >> sys.stderr, "Loading %d files in %s" % (len(filenames), dirpath)
        for f in filenames:
            f = os.path.join(dirpath, f)
#            print f
            txt = open(f).read()
            doc = {}
            doc["_id"] = f
            try:
                doc[options.field] = txt.decode("utf-8")
#                print doc
            except Exception, e:
                print >> sys.stderr, "Could not decode to UTF-8 this file %s" % f, type(e), e
#                print >> sys.stderr, "Could not decode to UTF-8 this file %s: %s" % (f, repr(doc))
            try:
                collection.save(doc)
#                print "%s now has %d docs" % (collection, collection.count())
            except Exception, e:
                print >> sys.stderr, "Could not save to mongodb this file %s" % f, type(e), e

    print "%s now has %d docs" % (collection, collection.count())
