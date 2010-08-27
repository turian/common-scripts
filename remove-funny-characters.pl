#!/usr/bin/perl -w
# Remove any funny character
while(<>) {
    s/([^\s\w\d\/\.\-\{\}\\\:\@\[\]\(\)\+\`\&\'\>\<\$\=\_\#\!\"\!\|\@\#\$\%\^\&\*\~\?\,\.\;])//g;
    print;
}
