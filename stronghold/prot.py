from Bio.Seq import Seq

with open("rosalind_prot.txt") as f:
    rna = f.read().strip()

seq = Seq(rna)
protein = seq.translate(to_stop=True)
print(protein)
