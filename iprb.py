with open('rosalind_iprb.txt', 'r') as f:
    k, m, n = map(int, f.read().strip().split())

total = k + m + n

# P(potomek aa) - wszystkie przypadki dające aa:
p_aa = (
    # mm x mm: 1/4 szans na aa
    (m/total) * ((m-1)/(total-1)) * 0.25 +
    # mm x aa: 1/2 szans na aa
    (m/total) * (n/(total-1)) * 0.5 +
    (n/total) * (m/(total-1)) * 0.5 +
    # aa x aa: zawsze aa
    (n/total) * ((n-1)/(total-1))
)

print(round(1 - p_aa, 5))
