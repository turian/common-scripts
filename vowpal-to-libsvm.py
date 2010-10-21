#!/usr/bin/env python
"""
Convert a vowpal-wabbit file in stdin to libsvm.
"""

import string, sys

fc = 1
fmap = {}

for l in sys.stdin:
    toks = string.split(l)
    print toks[0],
    assert toks[1] == "|features"
    for tok in toks[2:]:
        feat, val = string.split(tok, sep=":")
        if feat not in fmap:
            fmap[feat] = fc
            fc += 1
        print "%d:%s" % (fmap[feat], val)
