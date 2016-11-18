import skbio

seqs = skbio.io.read("gene1.fa", format="fasta")

for s in seqs:
    print(s.metadata)


# D1 = skbio.sequence.DNA("ACGTGTGTGT")
# R1 = skbio.sequence.RNA("ACGUGUGU")
# print(D1)
# print(R1)
