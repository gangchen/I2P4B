from Bio import SeqIO

for seq_record in SeqIO.parse("gene1.fa", "fasta"):
    print(seq_record.id)
