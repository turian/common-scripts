#!/usr/bin/perl -w


sub datestr {
        $str =  `date`;
        $str =~ s/\s+$//sg;
        return "$str ";
}

$lockdir = "locks";

if (not -d $lockdir) {
        system("mkdir $lockdir");
}
die "FATAL: '$lockdir' is not a directory!" unless -d $lockdir;

$cmd = join(' ', @ARGV);

$lockcmd = $cmd;
$lockcmd =~ s/\s\s+/ /g;
while ($lockcmd =~ m/[\s\.\/\\]/) { $lockcmd =~ s/[\s\.\/\\]/_/g; }

$lockfile = "$lockdir/lock-$lockcmd";

if (-e $lockfile) {
        print STDERR datestr(), "Existing lock file:\t'$lockfile'\n";
        print STDERR datestr(), "Skipping command:\t'$cmd'\n";
        exit;
} else {
        system("touch $lockfile");
        die "FATAL: Could not create lock file: '$lockfile'\n" unless -e $lockfile;
        print STDERR datestr(), "Created lock file:\t'$lockfile'\n";
        print STDERR datestr(), "Running command:\t'$cmd'\n";
        system("nice -10 time $cmd && rm $lockfile");
        print STDERR datestr(), "Command terminated:\t'$cmd'\n";
        if (-e $lockfile) {
                print STDERR datestr(), "Lock file still present. Forcing removal...\n";
                system("rm -f $lockfile");
                die "FATAL: Could not remove lock file: '$lockfile'\n" unless not -e $lockfile;
        }
}
