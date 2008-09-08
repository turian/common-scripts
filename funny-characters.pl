#!/usr/bin/perl -w
# Print lines with funny characters
# cf. no-funny-characters.pl
while(<>) {
    print "$1 $_" if m/([^\s\w\d\/\.\-\{\}\\\:\@\[\]\(\)\+\`\&\'\>\<\$\=\_\#\!\"\!\|\@\#\$\%\^\&\*\~\?\,\.\;])/;
}
