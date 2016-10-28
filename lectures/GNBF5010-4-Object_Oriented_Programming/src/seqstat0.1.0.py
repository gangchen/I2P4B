class seq:
    def __init__(self, seq, counts):
        self.seq = seq
        self.counts = counts


    def count(self):
        for base in self.seq:
            if base in self.counts.keys():
                self.counts[base] += 1

    def print1(self):
        for k in self.counts:
            print(k + ':' + str(self.counts[k]))

    def printPercent(self):
        totalNum = len(self.seq)
        for k in self.counts:
            print(k + ":" + str(self.counts[k]/totalNum))

class rnaseq(seq):
    def __init__(self, seq, counts = {'A':0, 'C':0,'G':0,'U':0,'N':0}):
        self.seq = seq
        self.counts = counts

class dnaseq(seq):
    def __init__(self, seq, counts = {'A':0, 'C':0,'G':0,'T':0,'N':0}):
        self.seq = seq
        self.counts = counts


print("dnaseq:")
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
ds.printPercent()

print("rnaseq:")
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
rs.printPercent()
