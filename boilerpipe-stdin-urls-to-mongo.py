#!/usr/bin/python
"""
Run every sys.stdin URL through Boilerpipe (or diffbot), and store in a MongoDB.
"""

import common.mongodb
import random

import common.html2text
import common.str
from common.stats import stats

import sys
import string

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--collection", dest="collection", help="collection name")
parser.add_option("-d", "--database", dest="database", help="database name")
parser.add_option("-p", "--port", dest="port", help="port number for mongodb", type="int")
parser.add_option("--hostname", dest="hostname", help="hostname for mongodb")
(options, args) = parser.parse_args()

def boilerpipe_all():
    collection = common.mongodb.collection(options.database, name=options.collection)

    for i, url in enumerate(sys.stdin):
        url = string.strip(url)
        # TODO: Find doc if it is already in collection
        doc = {}
        doc["_id"] = url

#        if (i+1) % 100 == 0:
#            print >> sys.stderr, "Retrieving boilerplate for doc # %s" % (common.str.percent(i+1, len(alldocids)))
#            print >> sys.stderr, stats()

        if doc is None:
            print >> sys.stderr, "WHA? no doc for %s" % id
            continue

        print >> sys.stderr, "Getting text for url %s ..." % doc["_id"].encode("utf-8")
        print >> sys.stderr, stats()
        try:
            doc["BoilerpipePageText"] = common.html2text.boilerpipe_url2text(doc["_id"])
#            doc["diffbot"] = common.html2text.diffbot_url2text(doc["_id"], token=DIFFBOT_TOKEN)
            collection.save(doc)
            print >> sys.stderr, "...done getting text for url %s" % doc["_id"].encode("utf-8")
        except:
            print >> sys.stderr, "ERROR for url %s" % doc["_id"].encode("utf-8")
        print >> sys.stderr, stats()

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)

    boilerpipe_all()
