from utils import parse_fasta

def overlap(a, b):
    max_overlap = min(len(a), len(b))
    for i in range(max_overlap, 0, -1):
        if a.endswith(b[:i]):
            return i
    return 0

def assemble(reads):
    reads = list(reads)
    while len(reads) > 1:
        best_overlap = 0
        best_i = 0
        best_j = 0

        for i in range(len(reads)):
            for j in range(len(reads)):
                if i != j:
                    o = overlap(reads[i], reads[j])
                    if o > best_overlap:
                        best_overlap = o
                        best_i = i
                        best_j = j

        merged = reads[best_i] + reads[best_j][best_overlap:]

        new_reads = []
        for k in range(len(reads)):
            if k != best_i and k != best_j:
                new_reads.append(reads[k])
        new_reads.append(merged)
        reads = new_reads

    return reads[0]

with open('rosalind_long.txt') as f:
    data = f.read()

sequences = parse_fasta(data)
reads = list(sequences.values())

print(assemble(reads))
