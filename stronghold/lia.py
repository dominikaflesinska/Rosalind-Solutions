from math import comb

def solve(k, N):
    n = 2 ** k       # number of organisms in generation k
    p = 0.25         # P(AaBb) = 1/4
    
    # P(X >= N) = 1 - P(X < N)
    prob_less = sum(
        comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        for i in range(N)
    )
    return 1 - prob_less

with open('rosalind_lia.txt') as f:
    k, N = map(int, f.read().split())

print(round(solve(k, N), 3))
