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

from optparse import OptionParser

import os, os.path

parser = OptionParser()
parser.add_option("-d", "--directory", dest="directory", help="directory that contains all documents (text files)", type="string")
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="database name")
parser.add_option("-p", "--port", dest="port", help="port number for mongodb", type="int")
parser.add_option("-f", "--field", dest="field", help="field name to use for loaded text", type="string", default="text")
parser.add_option("--hostname", dest="hostname", help="hostname for mongodb")
(options, args) = parser.parse_args()

def getdoc():
    for (dirpath, dirnames, filenames) in os.walk(options.directory, followlinks=True):
        if len(filenames) > 0:
            print >> sys.stderr, "Training on %d files in %s" % (len(filenames), dirpath)
        for f in filenames:
            f = os.path.join(dirpath, f)
#            print f
            doc = open(f).read()
            try:
                yield doc.decode("utf-8")
            except:
                print >> sys.stderr, "Could not decode to UTF-8 this file %s" % f
#                print >> sys.stderr, "Could not decode to UTF-8 this file %s: %s" % (f, repr(doc))

#for d in getdoc():
#    print len(d), repr(d)[:500]

print >> sys.stderr, "Saving term statistics to %s" % options.name
print >> sys.stderr, stats()
termextract.train.compute_term_statistics(options.name, getdoc())

print >> sys.stderr, "Let's threshold the vocabulary, while we're at it"
print >> sys.stderr, stats()
termextract.train.threshold(options.name)
