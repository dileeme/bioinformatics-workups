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

def psm_search(proteome, spectral_vectors, threshold):
    matches = []
    for spectral_vector in spectral_vectors:
        peptide, score = best_peptide_in_proteome(proteome, spectral_vector)
        if peptide is not None and score >= threshold:
            matches.append(peptide)
    return matches

proteome = "GAG"

vector1 = [-5] * 128
vector1[56] = 1
vector1[127] = 10

vector2 = [-5] * 57

threshold = 0

matches = psm_search(proteome, [vector1, vector2], threshold)
for peptide in matches:
    print(peptide)
