#!/usr/bin/env python
"""
Read one-line-per-word and convert to one-line-per-sentence.
"""

import sys,string
for l in sys.stdin:
    l = string.strip(l)
    if l == "": print
    else: print l,
