from collections import Counter

def cyclic_spectrum(peptide):
    n = len(peptide)
    prefix_mass = [0]
    for mass in peptide:
        prefix_mass.append(prefix_mass[-1] + mass)
    peptide_mass = prefix_mass[-1]

    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_mass = prefix_mass[j] - prefix_mass[i]
            spectrum.append(sub_mass)
            if i > 0 and j < n:
                spectrum.append(peptide_mass - sub_mass)
    return sorted(spectrum)

def linear_spectrum(peptide):
    n = len(peptide)
    prefix_mass = [0]
    for mass in peptide:
        prefix_mass.append(prefix_mass[-1] + mass)

    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)

def score_cyclic(peptide, spectrum):
    theoretical = Counter(cyclic_spectrum(peptide))
    experimental = Counter(spectrum)
    return sum(min(theoretical[mass], experimental[mass]) for mass in theoretical)

def score_linear(peptide, spectrum):
    theoretical = Counter(linear_spectrum(peptide))
    experimental = Counter(spectrum)
    return sum(min(theoretical[mass], experimental[mass]) for mass in theoretical)

def spectral_convolution(spectrum):
    diffs = []
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            diff = spectrum[i] - spectrum[j]
            if 57 <= diff <= 200:
                diffs.append(diff)
    return diffs

def top_m_masses(spectrum, m):
    counts = Counter(spectral_convolution(spectrum))
    ordered = sorted(counts.items(), key=lambda item: -item[1])
    if len(ordered) <= m:
        return [mass for mass, _ in ordered]
    threshold = ordered[m - 1][1]
    return [mass for mass, count in ordered if count >= threshold]

def trim(leaderboard, spectrum, n):
    scored = sorted(leaderboard, key=lambda peptide: -score_linear(peptide, spectrum))
    if len(scored) <= n:
        return scored
    cutoff = score_linear(scored[n - 1], spectrum)
    return [peptide for peptide in scored if score_linear(peptide, spectrum) >= cutoff]

def convolution_cyclopeptide_sequencing(spectrum, m, n):
    alphabet = top_m_masses(spectrum, m)
    parent_mass = max(spectrum)
    leaderboard = [[]]
    leader_peptide = []
    leader_score = -1

    while leaderboard:
        leaderboard = [peptide + [mass] for peptide in leaderboard for mass in alphabet]
        next_board = []
        for peptide in leaderboard:
            mass = sum(peptide)
            if mass == parent_mass:
                score = score_cyclic(peptide, spectrum)
                if score > leader_score:
                    leader_score = score
                    leader_peptide = peptide
                next_board.append(peptide)
            elif mass < parent_mass:
                next_board.append(peptide)
        leaderboard = trim(next_board, spectrum, n)

    return leader_peptide

M = 20
N = 60
spectrum = [0, 57, 113, 128, 147, 185, 204, 241, 260, 298, 317, 332, 388, 445]

peptide = convolution_cyclopeptide_sequencing(spectrum, M, N)
print("-".join(str(mass) for mass in peptide))
