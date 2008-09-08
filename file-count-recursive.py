#!/usr/bin/python
#
#  Like du, except a recursive file count.
#


import os
cnt = {}
fs = [i for i in os.walk(os.getcwd())]
fs.reverse()
for root, dirs, files in fs:
    mycnt = len(files)
    for d in dirs:
        mycnt += cnt[os.path.join(root, d)]
    cnt[root] = mycnt
    print "%d\t%s" % (mycnt, root)
