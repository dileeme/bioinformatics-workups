integer_mass = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128,
    "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
}

def best_peptide_in_proteome(proteome, spectral_vector):
    target_mass = len(spectral_vector)
    best_score, best_peptide = None, None
    for i in range(len(proteome)):
        total_mass = 0
        score = 0
        for j in range(i, len(proteome)):
            total_mass += integer_mass[proteome[j]]
            if total_mass > target_mass:
                break
            score += spectral_vector[total_mass - 1]
            if total_mass == target_mass:
                if best_score is None or score > best_score:
                    best_score, best_peptide = score, proteome[i:j + 1]
                break
    return best_peptide, best_score

proteome = "GASTGTASG"
spectral_vector = [-5] * 259
for position in (71, 101, 172):
    spectral_vector[position - 1] = 1
for position in (158, 259):
    spectral_vector[position - 1] = 10

peptide, score = best_peptide_in_proteome(proteome, spectral_vector)
print(peptide)
print(score)
