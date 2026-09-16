integer_mass = {"X": 4, "Z": 5}

def sequence_peptide(vector):
    n = len(vector)
    best = [float("-inf")] * (n + 1)
    best[0] = 0
    back = [None] * (n + 1)
    for j in range(1, n + 1):
        for amino_acid, mass in integer_mass.items():
            i = j - mass
            if i >= 0 and best[i] != float("-inf"):
                score = best[i] + vector[j - 1]
                if score > best[j]:
                    best[j] = score
                    back[j] = (i, amino_acid)
    peptide = []
    node = n
    while node != 0:
        i, amino_acid = back[node]
        peptide.append(amino_acid)
        node = i
    peptide.reverse()
    return "".join(peptide)

vector = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]

print(sequence_peptide(vector))
