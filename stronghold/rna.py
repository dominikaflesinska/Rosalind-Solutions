with open('rosalind_rna.txt', 'r') as f:
    dna = f.read().strip()

print(dna.replace('T', 'U'))
