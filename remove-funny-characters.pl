#!/usr/bin/perl -w
# Remove any funny character
while(<>) {
    s/([^\s\w\d\/\.\-\{\}\\\:\@\[\]\(\)\+\`\&\'\>\<\$\=\_\#\!\"\!\|\@\#\$\%\^\&\*\~\?\,\.\;])//g;
    s/\x0c//g;  # Remove form-feed, it trips up Python's lxml parser
    print;
}
