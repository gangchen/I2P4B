package snp;

use strict;
use warnings;

sub new{
    my $class = shift;
    my $self = {
        rsid => shift,
        chr => shift,
        pos => shift,
    };

    bless $self, $class;
    return $self;
}

sub getRsid{
    my $self = shift;
    return $self->{rsid};
}

sub getChr{
    my $self = shift;
    return $self->{chr};
}

sub getPos{
    my $self = shift;
    return $self->{pos};
}

sub setRsid{
    my $self = shift;
    $self->{rsid} = shift;
}

sub setChr{
    print $_,"\n" for @_;
    my $self = shift;
    $self->{chr} = shift;
}

sub summary{
    my $self = shift;
    print "The rsid is ", $self->{rsid}, "\n";
    print "The chr is ", $self->{chr}, "\n";
    print "The pos is ", $self->{pos}, "\n";
}

1;
