with open('rosalind_fib.txt', 'r') as f:
    n, k = map(int, f.read().strip().split())

rabbits = [0, 1, 1]

for i in range(2, n):
    rabbits.append(rabbits[-1] + k * rabbits[-2])

print(rabbits[n])
