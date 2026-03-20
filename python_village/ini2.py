with open('rosalind_ini2.txt', 'r') as f:
    a, b = map(int, f.read().strip().split())

result = a**2 + b**2
print(result)
