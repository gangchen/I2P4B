package wesnp;

use parent 'snp';

sub new{
    my $class = shift;

    my $self = $class->SUPER::new(shift, shift, shift);

    $self->{author} = shift;

    bless $self, $class;
    return $self;
}

sub getAuthor{
    my $self = shift;
    return $self->{author};
}

1;
