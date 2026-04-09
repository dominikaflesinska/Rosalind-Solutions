with open("rosalind_subs.txt") as f:
    s = f.readline().strip()
    t = f.readline().strip()

positions = []
start = 0
while True:
    index = s.find(t, start)
    if index == -1:
        break
    positions.append(index + 1)
    start = index + 1

print(" ".join(map(str, positions)))
