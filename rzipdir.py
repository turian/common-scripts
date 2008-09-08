#!/usr/bin/python
#
#################################################################
#
#  rzipdir.py
#
#  USAGE: rzipdir.py dir1 [dir2 ...]
#
#  Tar and rzip each directory given as a command-line parameter.
#  We use /data/turian/temp as a temporary directory.
#
#  $Id: rzip.pl,v 1.4 2004/12/15 13:44:12 turian Exp $
#
#
#################################################################

rzip = "/home/turian/utils/bin/rzip"
tempdir = "/data/turian/temp"

from debug import *
set_debug_level(20)

import os,os.path,shutil,sys
assert os.access(rzip, os.X_OK)
assert os.path.isdir(tempdir)

assert len(sys.argv) > 1

debug(1, "Dry run...")
for d in sys.argv[1:]:
	assert os.path.isdir(d)
	(base, nom) = os.path.split(d)
	if nom == "":
		(base, nom) = os.path.split(base)
	assert nom != ""
	if base == "": base = "."

	tar = os.path.join(tempdir, "%s.tar" % nom)

	cmd = "tar cf %s %s" % (tar, d)
	debug(1, cmd)
	#assert not os.path.isfile(tar)
	#r = os.system(cmd)
	#assert not r
	#assert os.path.isfile(tar)

	rziptar = "%s.rz" % tar
	cmd = "%s -P %s" % (rzip, tar)
	debug(1, cmd)
	#assert not os.path.isfile(rziptar)
	#r = os.system(cmd)
	#assert not r
	#assert os.path.isfile(rziptar)

	debug(1, "Removing directory %s" % d)
	#shutil.rmtree(d)
	#assert not os.path.exists(d)

	debug(1, "Moving %s to %s" % (rziptar, base))
	#shutil.move(rziptar, base)
	#assert not os.path.exists(rziptar)
	#assert os.path.exists(os.path.join(base, "%s.tar.rz" % nom))

debug(1, "\n")
debug(1, "True run...")
for d in sys.argv[1:]:
	assert os.path.isdir(d)
	(base, nom) = os.path.split(d)
	if nom == "":
		(base, nom) = os.path.split(base)
	assert nom != ""
	if base == "": base = "."

	tar = os.path.join(tempdir, "%s.tar" % nom)

	cmd = "tar cf %s %s" % (tar, d)
	debug(1, cmd)
	assert not os.path.isfile(tar)
	r = os.system(cmd)
	assert not r
	assert os.path.isfile(tar)

	rziptar = "%s.rz" % tar
	cmd = "%s -P %s" % (rzip, tar)
	debug(1, cmd)
	assert not os.path.isfile(rziptar)
	r = os.system(cmd)
	assert not r
	assert os.path.isfile(rziptar)

	debug(1, "Removing directory %s" % d)
	shutil.rmtree(d)
	assert not os.path.exists(d)

	debug(1, "Moving %s to %s" % (rziptar, base))
	shutil.move(rziptar, base)
	assert not os.path.exists(rziptar)
	assert os.path.exists(os.path.join(base, "%s.tar.rz" % nom))
