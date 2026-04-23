from itertools import permutations

with open('rosalind_perm.txt') as f:
    n = int(f.read().strip())

perms = list(permutations(range(1, n + 1)))
print(len(perms))
for p in perms:
    print(*p)
