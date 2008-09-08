#!/usr/bin/python2.4
#
#######################################################################
#
#
#   fix-filenames.py
#
#   USAGE: ./fix-filenames.py dir1 [dir2 ...]
#
#   Fix filenames and directory names, such that any "weird" character
#   is converted to an underscore.
#
#   A "weird" character is a non-alphanumeric character that is not
#   in the following list:
#	.-/[](),!_'&+#$~
#
#   For each directory given on the command-line, we fix the name of
#   *every* filename and directory name therein, recursing on subdirectories.
#
#
#   fix-filenames.py,v 1.1 2004/12/15 11:07:14 turian Exp
#
#
#######################################################################

import os,sys,re

if len(sys.argv) < 2:
	sys.stderr.write("Incorrect call.\nUSAGE: ./fix-filenames.py dir1 [dir2 ...]\n")
	assert(0)

list = []
dir = sys.argv[1:]

badre = re.compile("[^a-z0-9\s\.\-\/\[\]\(\)\,\!\_\'\&\+\#\$\~]", re.I)

def fixdirectory(d):
	done = False
	while not done:
		done = True
		for (dirpath, dirnames, filenames) in os.walk(d):
			#print (dirpath, dirnames, filenames)
			for f in dirnames + filenames:
				assert not badre.search(dirpath)

				origf = dirpath + "/" + f
				if not badre.search(origf): continue
				newf = badre.sub("_", origf)

				assert os.access(origf, os.W_OK)
				assert not os.access(newf, os.F_OK)

				sys.stderr.write("Renaming '%s' to '%s'\n" % (origf, newf))
				os.rename(origf, newf)
				assert not os.access(origf, os.F_OK)
				assert os.access(newf, os.F_OK)

				# If we've renamed a filename, then once
				# we are done with the current dirpath,
				# start again at the beginning of the
				# while loop.
				# This ensures that we don't have stale paths in
				# the os.walk list to the old directory name.
				if f in dirnames: done = False
			if not done: break

while len(dir):
	d = dir[0]
	dir = dir[1:]

	fixdirectory(d)
