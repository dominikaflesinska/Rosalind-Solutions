from utils import parse_fasta

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[b] for b in reversed(dna))

def find_reverse_palindromes(dna):
    results = []
    for i in range(len(dna)):
        for length in range(4, 13):
            if i + length > len(dna):
                break
            substring = dna[i:i+length]
            if substring == reverse_complement(substring):
                results.append((i + 1, length))
    return results

with open('rosalind_revp.txt') as f:
    data = f.read()

sequences = parse_fasta(data)
dna = list(sequences.values())[0]

for pos, length in find_reverse_palindromes(dna):
    print(pos, length)
