with open('rosalind_revc.txt', 'r') as f:
    dna = f.read().strip()

complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

result = ''
for base in reversed(dna):
    result += complement[base]

print(result)
