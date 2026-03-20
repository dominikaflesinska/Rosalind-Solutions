with open('rosalind_ini6.txt', 'r') as f:
    words = f.read().strip().split()

counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

for word in counter:
    print(word, counter[word])
