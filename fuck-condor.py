#!/usr/bin/python
#
#  Babysit condor.
#
#  Err file (stderr log) must be updated WRITEME
#
##

# WRITEME
loglines = 100

# WRITEME
delay_minutes = 10

import os, popen2, string, os.path, time

from debug import *
set_debug_level(99)

allvars = ["ClusterId", "ProcId", "Err", "Iwd", "Cmd"]

class Job:
	"A condor job"

	id = None
	origerr = None
	errlog = None

	def __init__(self, jobvar):
		self.id = "%s.%s" % (jobvar["ClusterId"], jobvar["ProcId"])
		self.origerr = jobvar["Err"][1:-1]
		self.errlog = os.path.join(jobvar["Iwd"][1:-1], jobvar["Err"][1:-1])
		assert os.access(self.errlog, os.R_OK)

	def errtext(self):
		assert os.access(self.errlog, os.R_OK)
		(tin, tout) = popen2.popen2("tail -%d %s" % (loglines, self.errlog))
		logtxt = string.join(tin.readlines(), "")
		tout.close()
		return logtxt

Cmd = "/s1/condor/bin/condor_dagman"

def find_all_jobs():
	alljobs = []
	jobvar = {}
	for v in allvars: jobvar[v] = None
	(qin, qout) = popen2.popen2("condor_q -long -run")
	for l in qin:
		l = string.strip(l)
		if l == "":
			if jobvar["ClusterId"]:
				for v in allvars: assert jobvar[v]
				# Skip dagman
				if jobvar["Cmd"][1:-1] == "/s1/condor/bin/condor_dagman":
					continue
				alljobs.append(Job(jobvar))
			else:
				for v in allvars: assert not jobvar[v]
			for v in allvars: jobvar[v] = None
		else:
			for v in allvars:
				if l.find(v) == 0: jobvar[v] = l[len(v + " = "):]
	qin.close()
	qout.close()
	return alljobs

last_log = {}
while 1:
	alljobs = find_all_jobs()
	new_log = {}
	for job in alljobs:
		txt = job.errtext()
		log = job.errlog
		new_log[log] = txt
		if log in last_log:
			if last_log[log] == txt:
				debug(1, "WARNING: %s %s has not changed since %d minutes ago...\n\tRemoving..." % (job.id, job.origerr, delay_minutes))
				os.system("/s1/condor/bin/condor_rm %s" % job.id)
			else:
				debug(1, "\t%s %s has changed since %d minutes ago." % (job.id, job.origerr, delay_minutes))
	last_log = new_log
	time.sleep(delay_minutes*60)
