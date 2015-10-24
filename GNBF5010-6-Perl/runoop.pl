use warnings;
use strict;

use snp;


my $snpA = new snp("rs671", "12", "111803962");

print $snpA->getRsid, "\n";

$snpA->setRsid("rs672");

print $snpA->getRsid, "\n";

$snpA->summary;
