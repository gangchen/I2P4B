package SNPAnno;

use warnings;
use strict;

sub annotateFile($){
  my $snpFilename = shift;
  open snpFile, $snpFilename or die $!;
  my @snp = <snpFile>;
  close snpFile;

  open annoDB, "hg19_refGene.txt" or die $!;
  my %anno;
  while(<annoDB>){
    my @fields = split "\t";
    my $refChr = $fields[2] =~ m/chr(\d+)/;
    my $start = $fields[4];
    my $end = $fields[5];
    $anno{$refChr."\t".$start."\t".$end} = $fields[12];
  }
  close annoDB;

  for my $snp (@snp){
    chomp($snp);
    my ($chr, $pos) = split "\t", $snp;
    for my $refPos (keys %anno){
      my($refChr, $start, $end) = split "\t",$refPos;
      if($chr eq $refChr){
        if($pos >= $start && $pos <= $end){
          print $chr, "\t", $pos, "\t", $anno{$refPos},"\n";
        }
      }
    }
  }

  return 0;
}

1;
