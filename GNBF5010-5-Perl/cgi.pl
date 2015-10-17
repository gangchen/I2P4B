#!/usr/bin/perl

=head CGI Example for GNBF5010 @ CUHK
Author: Gang CHEN (cg@wegene.com)
Date: Oct 16, 2015
Usage: Set up CGI environment on you system. Then, copy this script to your CGI directory. Open your broswer, visit and execute this script.
=cut

use CGI qw(:standard);

print header;
print start_html('A CGI Example for GNBF5010 @ CUHK'),
    h1('Sign Up'),
    start_form,
    "What's your name? ",textfield('name'),
    p,
    "What's your favorite language?",
    p,
    checkbox_group(-name=>'language',
		   -values=>['C','C++','Perl','Python', 'Java', 'R', 'Go', 'JavaScript', 'Other'],
		   -defaults=>['Python','Go', 'R']),
    p,
    "Who's your favorite lecturer? ",
    popup_menu(-name=>'lecturer',
	       -values=>['Gang CHEN','other', 'other']),
    p,
    submit,
    end_form,
    hr;

if (param()) {

    open LOGFILE, ">>log.txt";
    print LOGFILE param('name'), "\t", join(",",param('language')), "\t", param('lecturer'), "\n";
    close LOGFILE;

    print
	"Your name is",em(param('name')),
	p,
	"The keywords are: ",em(join(", ",param('language'))),
	p,
	"Your favorite color is ",em("Gang CHEN"),
	hr;
}
