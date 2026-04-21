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

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[b] for b in reversed(dna))

def translate(codon):
    table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }
    return table.get(codon, '')

def find_orfs(dna):
    proteins = set()
    for strand in [dna, reverse_complement(dna)]:
        for frame in range(3):
            i = frame
            while i + 3 <= len(strand):
                codon = strand[i:i+3]
                if translate(codon) == 'M':
                    protein = ''
                    for j in range(i, len(strand) - 2, 3):
                        aa = translate(strand[j:j+3])
                        if aa == '*':
                            if protein:
                                proteins.add(protein)
                            break
                        protein += aa
                i += 3
    return proteins

with open('rosalind_orf.txt') as f:
    data = f.read()

sequences = parse_fasta(data)
dna = list(sequences.values())[0]

for protein in find_orfs(dna):
    print(protein)
