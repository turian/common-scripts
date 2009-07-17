#!/bin/sh
# Count the number of jobs each user has in the queue (running or idle)
condor_q -global | grep : | grep '\/' | ~/common/scripts/choose-columns.py 2 | sort | uniq -c | sort -n
