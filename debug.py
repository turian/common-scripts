#
#   debug.py
#
#   Debug messages.
#
#   $Id: debug.py,v 1.4 2005/07/26 18:26:54 turian Exp $
#
# Copyright (c) 2004, 2005, New York University. All rights reserved
#######################################################################

import realtime
import sys

def set_debug_level(x):
	global debug_level
	debug_level = x

def error(msg):
	sys.stderr.write("ERROR occurred at %s:\n%s\n" % (realtime.elapsed_str(), msg))

def debug(lvl, msg):
	if lvl <= debug_level:
		sys.stderr.write("%s: %s\n" % (realtime.elapsed_str(), msg))
