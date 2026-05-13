def longest_increasing_subsequence(perm):
    n = len(perm)
    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if perm[j] < perm[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    idx = dp.index(max(dp))

    result = []
    while idx != -1:
        result.append(perm[idx])
        idx = parent[idx]

    return result[::-1]

def longest_decreasing_subsequence(perm):
    negated = [-x for x in perm]
    return [-x for x in longest_increasing_subsequence(negated)]

with open('rosalind_lgis.txt') as f:
    lines = f.read().strip().split('\n')

n = int(lines[0])
perm = list(map(int, lines[1].split()))

print(*longest_increasing_subsequence(perm))
print(*longest_decreasing_subsequence(perm))
