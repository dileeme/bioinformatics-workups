from collections import Counter

AMINO_ACID_MASSES = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def linear_spectrum(peptide):
    prefix_mass = [0]
    for mass in peptide:
        prefix_mass.append(prefix_mass[-1] + mass)
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return spectrum

def cyclic_spectrum(peptide):
    prefix_mass = [0]
    for mass in peptide:
        prefix_mass.append(prefix_mass[-1] + mass)
    peptide_mass = prefix_mass[-1]
    n = len(peptide)
    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(spectrum)

def is_consistent(peptide, spectrum_counts):
    linear_counts = Counter(linear_spectrum(peptide))
    return all(count <= spectrum_counts.get(mass, 0) for mass, count in linear_counts.items())

def expand(peptides):
    return [peptide + [mass] for peptide in peptides for mass in AMINO_ACID_MASSES]

def cyclopeptide_sequencing(spectrum):
    spectrum_counts = Counter(spectrum)
    parent_mass = max(spectrum)
    candidates = [[]]
    results = []

    while candidates:
        candidates = expand(candidates)
        surviving = []
        for peptide in candidates:
            mass = sum(peptide)
            if mass == parent_mass:
                if cyclic_spectrum(peptide) == sorted(spectrum):
                    results.append(peptide)
            elif is_consistent(peptide, spectrum_counts):
                surviving.append(peptide)
        candidates = surviving

    return results

spectrum = [0, 113, 128, 186, 241, 299, 314, 427]

peptides = cyclopeptide_sequencing(spectrum)
print(" ".join("-".join(str(m) for m in peptide) for peptide in peptides))
