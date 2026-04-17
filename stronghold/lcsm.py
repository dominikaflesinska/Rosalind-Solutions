def parse_fasta(data):
    sequences = {}
    current_label = None
    for line in data.strip().split('\n'):
        if line.startswith('>'):
            current_label = line[1:]
            sequences[current_label] = ''
        else:
            sequences[current_label] += line
    return sequences

def longest_common_substring(sequences):
    seqs = list(sequences.values())
    shortest = min(seqs, key=len)
    n = len(shortest)
    
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            motif = shortest[start:start + length]
            if all(motif in s for s in seqs):
                return motif

with open('rosalind_lcsm.txt') as f:
    data = f.read()

sequences = parse_fasta(data)
print(longest_common_substring(sequences))
