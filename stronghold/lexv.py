from itertools import product

with open('rosalind_lexv.txt') as f:
    lines = f.read().strip().split('\n')

alphabet = lines[0].split()
n = int(lines[1])

for combo in product(alphabet, repeat=n):
    print(''.join(combo))
