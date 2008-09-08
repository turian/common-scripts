#!/bin/sh
#
# $Id: shuffle.sh,v 1.2 2004/02/08 08:18:30 turian Exp $
#

SHUFFLE_DIR="$HOME/common/scripts/shuffle"

$SHUFFLE_DIR/random_key.pl | sort -T /tmp -n | $SHUFFLE_DIR/clean.pl
#$SHUFFLE_DIR/random_key.pl | sort -T /data/$USER -n | $SHUFFLE_DIR/clean.pl
