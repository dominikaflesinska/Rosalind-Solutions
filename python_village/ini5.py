with open('rosalind_ini5.txt', 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        print(lines[i].strip())
