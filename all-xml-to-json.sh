#!/usr/bin/env bash
#
#  For every XML file in the command-line, convert it to JSON.
#
#   USAGE:
#       all-xml-to-json.sh *xml

for f in "$@"
do
    echo "cat ${f} | remove-non-utf10-characters.pl | ~/dev/python/common/xml2json/parker.py > ${f}.json"
    cat ${f} | remove-non-utf10-characters.pl | ~/dev/python/common/xml2json/parker.py > ${f}.json
done
