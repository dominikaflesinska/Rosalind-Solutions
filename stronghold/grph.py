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

def overlap_graph(sequences, k=3):
    edges = []
    labels = list(sequences.keys())
    for s in labels:
        for t in labels:
            if s != t and sequences[s][-k:] == sequences[t][:k]:
                edges.append((s, t))
    return edges

with open('rosalind_grph.txt') as f:
    data = f.read()

sequences = parse_fasta(data)
for edge in overlap_graph(sequences):
    print(edge[0], edge[1])
