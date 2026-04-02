with open('rosalind_gc.txt', 'r') as f:
    lines = f.read().strip().split('\n')

sequences = {}
current_id = ''

for line in lines:
    if line.startswith('>'):
        current_id = line[1:]
        sequences[current_id] = ''
    else:
        sequences[current_id] += line

best_id = ''
best_gc = 0

for seq_id in sequences:
    dna = sequences[seq_id]
    gc = (dna.count('G') + dna.count('C')) / len(dna) * 100
    if gc > best_gc:
        best_gc = gc
        best_id = seq_id

print(best_id)
print('%f' % best_gc)
