from Bio import SeqIO

def main():
    sequences = [str(r.seq) for r in SeqIO.parse("rosalind_cons.txt", "fasta-pearson")]
    n = len(sequences[0])

    profile = {nuc: [0] * n for nuc in "ACGT"}
    for seq in sequences:
        for i, nuc in enumerate(seq):
            profile[nuc][i] += 1

    consensus = ""
    for i in range(n):
        consensus += max("ACGT", key=lambda nuc: profile[nuc][i])

    print(consensus)
    for nuc in "ACGT":
        print(f"{nuc}: {' '.join(map(str, profile[nuc]))}")

if __name__ == "__main__":
    main()
