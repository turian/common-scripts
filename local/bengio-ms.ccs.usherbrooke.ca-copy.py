#!/usr/bin/python
#
# Copy files and directories to no.shit.la, keeping the same exact path
# location (wrt homedir).
#
# $Id$
#

home = "/u/turian"
#home = "/home/fringant2/lisa/turian"
remote = "bengio-ms.ccs.usherbrooke.ca"

import sys, re, os

if len(sys.argv) == 1:
	sys.stderr.write("No input files given!\n")
	assert 0

import os.path

#home = os.path.normpath(os.environ["HOME"])
#sys.stderr.write("Stripping homedir = %s\n" % home)
#homedir_re = re.compile("^%s/" % home)

homedir_re = re.compile("^%s/" % home)
files = ""
for f in sys.argv[1:]:
    f = os.path.abspath(f)
    print f
    assert homedir_re.match(f)
    f = homedir_re.sub("", f)	# Cut off the homedir
    files += " " + f

cmd = "tar cf - %s | ssh %s -C 'tar xvf -'" % (files, remote)
os.chdir(home)
sys.stderr.write("%s\n" % cmd)
os.system(cmd)
