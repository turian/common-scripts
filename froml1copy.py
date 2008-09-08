#!/usr/bin/python
#
# Copy files and directories to l1.ccss, keeping the same exact path
# location (wrt homedir).
#
# $Id$
#

home = "/home/turian"
remote = "l1.ccss"

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
	assert homedir_re.match(f)
	f = homedir_re.sub("", f)	# Cut off the homedir
	files += " " + f

cmd = "tar cf - %s | ssh %s 'tar xvf -'" % (files, remote)
os.chdir(home)
sys.stderr.write("%s\n" % cmd)
#os.system(cmd)
