#!/usr/bin/env python
"""
Read in the XML mysqldump from sys.sdin.

@note: We assume that <row> and </row> are in lines with no other text, save whitespace.
"""

rows = []

# Current row
rowtxt = None

import sys
import re
row_start_re = re.compile('^\s*<row>\s*$')
row_end_re = re.compile('^\s*</row>\s*$')

from common.xml2json.parker import convertxmlstring 
import common.json

for l in sys.stdin:
    if row_start_re.match(l):
        assert rowtxt is None
        rowtxt = ""

    if rowtxt is not None: rowtxt += l

    if row_end_re.match(l):
        row = convertxmlstring(rowtxt)["row"]
        print common.json.dumps(row, indent=4)
        #convertxmlstring(rowtxt)
        rowtxt = None
