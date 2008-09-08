#
#   realtime.py
#
#   Track elapsed time.
#
#   $Id: realtime.py,v 1.4 2005/07/26 18:26:54 turian Exp $
#
##########
# Copyright (c) 2004, 2005, New York University. All rights reserved
#######################################################################

import time

t0 = time.time()

def elapsed_int():
	return time.time() - t0

def elapsed_str():
	t = time.time() - t0
	h = int(t / 3600)
	m = int((t - h * 3600) / 60)
	s = int(t - h * 3600 - m * 60)
	ms = t - h * 3600 - m * 60 - s
	ms = ("%.2f" % ms)
	return "%.2d:%.2d:%.2d.%s" % (h, m, s, ms[2:])

def elapsed():
	return "%.2f seconds" % (time.time() - t0)
