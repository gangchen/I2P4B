use warnings;
use strict;

use snp;
use wesnp;


my $snpA = new snp("rs671", "12", "111803962");

print $snpA->getRsid, "\n";

$snpA->setRsid("rs672");

print $snpA->getRsid, "\n";

$snpA->summary;

my $wesnpA = new wesnp("rs671", "12", "111803962", "Gang CHEN");
print $wesnpA->getRsid, "\n";
print $wesnpA->getAuthor, "\n";
