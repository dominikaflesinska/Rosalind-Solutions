with open('rosalind_ini4.txt', 'r') as f:
    a, b = map(int, f.read().strip().split())

suma = 0
for i in range(a, b+1):
    if i % 2 != 0:
        suma = suma + i

print(suma)
