integer_mass = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128,
    "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
}

def sequence_peptide(spectral_vector):
    target_mass = len(spectral_vector)
    dp = [float("-inf")] * (target_mass + 1)
    dp[0] = 0
    backtrack = [None] * (target_mass + 1)
    for i in range(1, target_mass + 1):
        for amino_acid, mass in integer_mass.items():
            if i - mass >= 0 and dp[i - mass] != float("-inf"):
                candidate = dp[i - mass] + spectral_vector[i - 1]
                if candidate > dp[i]:
                    dp[i] = candidate
                    backtrack[i] = (i - mass, amino_acid)
    peptide = []
    i = target_mass
    while i > 0:
        prev, amino_acid = backtrack[i]
        peptide.append(amino_acid)
        i = prev
    peptide.reverse()
    return "".join(peptide)

target_mass = 291
spectral_vector = [-5] * target_mass
for position in (128, 291):
    spectral_vector[position - 1] = 50

print(sequence_peptide(spectral_vector))
