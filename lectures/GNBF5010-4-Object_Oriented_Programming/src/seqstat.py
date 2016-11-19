class seq:
    def __init__(self, seq, counts):
        self.seq = seq
        self.counts = counts
        self.len = len(self.seq)
        self.i = 0
        self.c = seq[self.i]

    def count(self):
        for base in self.seq:
            if base in self.counts.keys():
                self.counts[base] += 1

    def print1(self):
        for k in self.counts:
            print(k + ':' + str(self.counts[k]))

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.len:
            c = self.seq[self.i]
            self.i += 1
            return c
        else:
            raise StopIteration()

class dnaseq(seq):
    def __init__(self, seq, counts = {'A':0, 'C':0,'G':0,'T':0,'N':0}):
        super.__init__(seq, counts)

class rnaseq(seq):
    def __init__(self, seq, counts = {'A':0, 'C':0,'G':0,'U':0,'N':0}):
        self.seq = seq
        self.counts = counts


ds = dnaseq(""" >chr21
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCGTGCAGTCAGTG
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TTGTGACTGAAGGGCATGTGTTCAGGCAAGATTGTTGGGTGGCTGTGTTT
TGTCTTCTTCCAGCTCGGCCATGGAATAGCCTGTGGGGACCTACTCTGTG
GTCCCCAGGGAGCTACTCTGTGGGGGCTGTTTCTGTTCAGCAGGGAAGGC
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TCACAGATGACAGTTACTTCCCTAGGTAGTCTGCATGTTGGGCCTCCCAG""")

ds.count()
ds.print1()

for a in ds:
    print(a)

rs = rnaseq(""" >chr21
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCGTGCAGTCAGTG
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TTGTGACTGAAUUUUUUUUUUTCAGGCAAGATTGTTGGGTGGCTGTGTTT
TGTCTTCTTCCAGCTCGGCCATGGAATAGCCTGTGGGGACCTACTCTGTG
GTCCCCAGGGAGCTACTCTGTGGGGGCTGTTTCTGTTCAGCAGGGAAGGC
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TCACAGATGACAGTTACTTCCCTAGGTAGTCTGCATGTTGGGCCTCCCAG""")
rs.count()
rs.print1()