#!/usr/bin/env python
"""
Read in the XML mysqldump for sys.sdin.

@note: We assume that <row> and </row> are in lines with no other text, save whitespace.
"""

import sys
try:
    import psyco
    psyco.full()
except ImportError:
    sys.stderr.write("psyco could not be imported\n")

rows = []

# Current row
rowtxt = None

import re
row_start_re = re.compile('^\s*<row>\s*$')
row_end_re = re.compile('^\s*</row>\s*$')

title_re = re.compile('<title>(.*)</title>')
hackernews_re = re.compile('Hacker News \|\s*')
link_re = re.compile('\|\s+link')

from common.xml2json.parker import convertxmlstring
from common.html2text import html2text
import common.json

for l in sys.stdin:
    if row_start_re.match(l):
        assert rowtxt is None
        rowtxt = ""

    if rowtxt is not None: rowtxt += l

    if row_end_re.match(l):
        row = convertxmlstring(rowtxt)["row"]
        (id, created_at, url, text) = row
        print >> sys.stderr, "Processing id #%s" % id
#        print "id=", id
#        print "created_at=", created_at
#        print "url=", url

        if text == "" or text is None:
            rowtxt = None
            continue

        m = title_re.search(text)
        if not m:
            title = None
        else:
            title = m.group(1)
            title = hackernews_re.sub("", title)
#            print "title=", title.encode("utf-8")

#        print "text=", text.encode("utf-8")
        try:
            txttext = html2text(text)
    #        print "len(txttext)=", len(txttext)
     #       print "commentcount=", len(link_re.findall(txttext))
     #       print "txttext=", txttext
     #       print 
        except RuntimeError:
            print >> sys.stderr, "RuntimeError when processing text:", text.encode("utf-8")
            rowtxt = None
            continue

        rowtxt = None
