#!/usr/bin/python
"""
For line in stdin, convert it to a JSON dict with key: "content" and value: line.
"""

from common.json import dumps

import sys
import string

print >> sys.stderr, "Reading from stdin..."
for l in sys.stdin:
    print dumps({"content": string.strip(l).decode("utf-8")})
