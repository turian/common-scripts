#!/bin/sh
#

SHUFFLE_DIR="$HOME/common/scripts/shuffle"

$SHUFFLE_DIR/random_key.pl | sort -T /tmp -n | $SHUFFLE_DIR/clean.pl
#$SHUFFLE_DIR/random_key.pl | sort -T /data/$USER -n | $SHUFFLE_DIR/clean.pl
