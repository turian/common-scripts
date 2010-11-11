#!/usr/bin/env python
"""
Convert a vowpal-wabbit file in stdin to libsvm.

USAGE:
    ./vowpal-to-libsvm.py < file.txt > file.libsvm
"""

import string, sys

from common.idmap import IDmap
from common.file import myopen

fmap = IDmap(allow_unknown=False)

for l in sys.stdin:
    toks = string.split(l)
    print toks[0],
    assert toks[1] == "|features"
    newfeats = []
    for tok in toks[2:]:
        feat, val = string.split(tok, sep=":")
        if not fmap.exists(feat): fmap.add(feat)
        newfeats.append((fmap.id(feat), val))
    newfeats.sort()
    for feat, val in newfeats:
        print "%d:%s" % (feat, val),
    print
