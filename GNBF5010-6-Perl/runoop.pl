use warnings;
use strict;

use wesnp;

my $wesnp = new wesnp("rs671", "12", "1234567", "Gang CHEN");

print $wesnp->getRsid, "\n";

print $wesnp->getAuthor, "\n";
$wesnp->summary;

my $snp = new snp("rs671", "12", "1234567");
print $snp->getRsid, "\n";
print $snp->getAuthor, "\n";
