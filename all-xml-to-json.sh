#!/usr/bin/env bash
#
#  For every XML file in the command-line, convert it to JSON.
#
#   USAGE:
#       all-xml-to-json.sh *xml

for f in "$@"
do
    echo "~/dev/python/common/xml2json/parker.py < ${f} > ${f}.json"
    ~/dev/python/common/xml2json/parker.py < ${f} > ${f}.json
done
