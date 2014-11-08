from Bio.Seq import Seq

#create a sequence object
my_seq = Seq('CATGTAGACTAG')

#print out some details about it
print 'seq %s is %i bases long' % (my_seq, len(my_seq))
print 'reverse complement is %s' % my_seq.reverse_complement()
print 'protein translation is %s' % my_seq.translate()
