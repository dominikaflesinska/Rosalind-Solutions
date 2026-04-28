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
