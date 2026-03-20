with open('rosalind_ini3.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    s = lines[0]
    a, b, c, d = map(int, lines[1].split())

print(s[a:b+1], s[c:d+1])
