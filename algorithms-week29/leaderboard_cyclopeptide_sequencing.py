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

def score(peptide, spectrum_counts, cyclic):
    theoretical = Counter(cyclic_spectrum(peptide) if cyclic else linear_spectrum(peptide))
    return sum(min(count, spectrum_counts.get(mass, 0)) for mass, count in theoretical.items())

def expand(peptides):
    return [peptide + [mass] for peptide in peptides for mass in AMINO_ACID_MASSES]

def trim(leaderboard, spectrum_counts, n):
    scored = sorted(leaderboard, key=lambda peptide: score(peptide, spectrum_counts, False), reverse=True)
    if len(scored) <= n:
        return scored
    cutoff_score = score(scored[n - 1], spectrum_counts, False)
    return [peptide for peptide in scored if score(peptide, spectrum_counts, False) >= cutoff_score]

def leaderboard_cyclopeptide_sequencing(spectrum, n):
    spectrum_counts = Counter(spectrum)
    parent_mass = max(spectrum)
    leaderboard = [[]]
    leader_peptide = []
    leader_score = 0

    while leaderboard:
        leaderboard = expand(leaderboard)
        surviving = []
        for peptide in leaderboard:
            mass = sum(peptide)
            if mass == parent_mass:
                peptide_score = score(peptide, spectrum_counts, True)
                if peptide_score > leader_score:
                    leader_score = peptide_score
                    leader_peptide = peptide
                surviving.append(peptide)
            elif mass < parent_mass:
                surviving.append(peptide)
        leaderboard = trim(surviving, spectrum_counts, n)

    return leader_peptide

n = 10
spectrum = [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484]

leader_peptide = leaderboard_cyclopeptide_sequencing(spectrum, n)
print("-".join(str(mass) for mass in leader_peptide))
