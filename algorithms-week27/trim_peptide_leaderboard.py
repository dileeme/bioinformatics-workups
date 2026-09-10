from collections import Counter

amino_acid_mass = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128, "E": 129,
    "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
}

def linear_spectrum(peptide):
    prefix_mass = [0]
    for acid in peptide:
        prefix_mass.append(prefix_mass[-1] + amino_acid_mass[acid])
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return spectrum

def linear_score(peptide, spectrum):
    theoretical = Counter(linear_spectrum(peptide))
    actual = Counter(spectrum)
    return sum(min(count, actual[mass]) for mass, count in theoretical.items())

def trim(leaderboard, spectrum, n):
    scored = sorted(leaderboard, key=lambda peptide: linear_score(peptide, spectrum), reverse=True)
    if len(scored) <= n:
        return scored
    cutoff_score = linear_score(scored[n - 1], spectrum)
    return [peptide for peptide in scored if linear_score(peptide, spectrum) >= cutoff_score]

leaderboard = ["LAST", "ALST", "TLLT", "TQAS"]
spectrum = [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372]
n = 2

print(" ".join(trim(leaderboard, spectrum, n)))
