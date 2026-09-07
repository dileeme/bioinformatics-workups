from collections import Counter

mass_table = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128,
    "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

def linear_spectrum(peptide):
    masses = [mass_table[a] for a in peptide]
    n = len(masses)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + masses[i]
    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix[j] - prefix[i])
    return sorted(spectrum)

def linear_peptide_score(peptide, spectrum):
    theoretical = Counter(linear_spectrum(peptide))
    given = Counter(spectrum)
    return sum(min(theoretical[m], given[m]) for m in theoretical)

peptide = "NQEL"
spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]

print(linear_peptide_score(peptide, spectrum))
