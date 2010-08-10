#!/usr/bin/python
"""
Convert a TSV file to HTML.
"""

import sys
import string

print >> sys.stderr, "Reading sys.stdin..."
print "<table>"
for l in sys.stdin:
    print "<tr>",
    for field in string.split(l, "\t"):
        print "<td>%s</td>" % string.strip(field),
    print "</tr>"
print "</table>"
