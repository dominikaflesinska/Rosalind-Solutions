with open('rosalind_hamm.txt', 'r') as f:
    lines = f.read().strip().split('\n')

s = lines[0]
t = lines[1]

hamming = 0
for i in range(len(s)):
    if s[i] != t[i]:
        hamming += 1

print(hamming)
