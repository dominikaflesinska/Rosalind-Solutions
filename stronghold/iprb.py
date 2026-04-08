with open('rosalind_iprb.txt', 'r') as f:
    k, m, n = map(int, f.read().strip().split())

total = k + m + n

# P(offspring aa) - all cases producing aa:
p_aa = (
    # Aa x Aa: 1/4 chance of aa
    (m/total) * ((m-1)/(total-1)) * 0.25 +
    # Aa x aa: 1/2 chance of aa
    (m/total) * (n/(total-1)) * 0.5 +
    # aa x Aa: 1/2 chance of aa
    (n/total) * (m/(total-1)) * 0.5 +
    # aa x aa: always aa
    (n/total) * ((n-1)/(total-1))
)

print(round(1 - p_aa, 5))

