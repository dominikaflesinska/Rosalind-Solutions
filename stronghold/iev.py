probs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

with open('rosalind_iev.txt') as f:
    couples = list(map(int, f.read().split()))

expected = sum(c * 2 * p for c, p in zip(couples, probs))
print(expected)
