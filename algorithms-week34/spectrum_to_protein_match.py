from collections import Counter

monoisotopic_mass = {
    "G": 57.02146, "A": 71.03711, "S": 87.03203, "P": 97.05276,
    "V": 99.06841, "T": 101.04768, "C": 103.00919, "L": 113.08406,
    "I": 113.08406, "N": 114.04293, "D": 115.02694, "Q": 128.05858,
    "K": 128.09496, "E": 129.04259, "M": 131.04049, "H": 137.05891,
    "F": 147.06841, "R": 156.10111, "Y": 163.06333, "W": 186.07931
}

def complete_spectrum(peptide):
    masses = [monoisotopic_mass[a] for a in peptide]
    prefix, total = [], 0.0
    for m in masses:
        total += m
        prefix.append(round(total, 5))
    suffix, total = [], 0.0
    for m in reversed(masses):
        total += m
        suffix.append(round(total, 5))
    return prefix + suffix

def max_shared_multiplicity(spectrum, peptide):
    other = complete_spectrum(peptide)
    diffs = Counter(round(r - s, 3) for r in spectrum for s in other)
    return max(diffs.values())

def best_matching_protein(spectrum, proteins):
    return max(proteins, key=lambda peptide: max_shared_multiplicity(spectrum, peptide))

proteins = ["PRTEIN", "GATHVK", "SDLMCW", "AAAAAA"]
spectrum = [
    97.05276, 253.15387, 354.20155, 483.24414, 596.3282, 710.37113,
    114.04293, 227.12699, 356.16958, 457.21726, 613.31837, 710.37113,
]

best = best_matching_protein(spectrum, proteins)
print(max_shared_multiplicity(spectrum, best))
print(best)
