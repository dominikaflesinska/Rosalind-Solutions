from Bio import ExPASy, SeqIO
import re

def get_sequence(protein_id):
    uid = protein_id.split('_')[0]
    handle = ExPASy.get_sprot_raw(uid)
    record = SeqIO.read(handle, "swiss")
    return str(record.seq)

def find_motif(sequence):
    pattern = re.compile(r'(?=(N[^P][ST][^P]))')
    return [m.start() + 1 for m in pattern.finditer(sequence)]

with open('rosalind_mprt.txt') as f:
    ids = f.read().strip().split('\n')

for protein_id in ids:
    sequence = get_sequence(protein_id)
    positions = find_motif(sequence)
    if positions:
        print(protein_id)
        print(*positions)
