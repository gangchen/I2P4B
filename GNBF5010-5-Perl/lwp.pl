=head
Scrape publication titles according to PubMed ids.

For CUHK-I2P course.

Usage:
  perl lwp.pl filename

Argument:
  filename: a file of PubMed ids. Each line is a PubMed id.

Author: Gang Chen
=cut

use warnings;
use strict;

use LWP::Simple;

my $filename = shift;

open my $idFile, $filename or die $!;

while(<$idFile>){

  chomp;

  my $content = get("http://www.ncbi.nlm.nih.gov/pubmed/".$_);

  $content =~ m/<h1>(.+)<\/h1>/;

  print $_,"\t",$1,"\n";
}
close $idFile;
