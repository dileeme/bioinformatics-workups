mass_table = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128, "E": 129,
    "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

def ideal_spectrum(peptide):
    n = len(peptide)
    prefix = [0] * (n + 1)
    for i, aa in enumerate(peptide):
        prefix[i + 1] = prefix[i] + mass_table[aa]
    total = prefix[-1]
    spectrum = [0, total]
    for i in range(1, n):
        spectrum.append(prefix[i])
        spectrum.append(total - prefix[i])
    return sorted(spectrum)

def decode_ideal_spectrum(spectrum):
    values = sorted(set(spectrum))
    total = max(values)
    graph = {}
    for u in values:
        for v in values:
            if v > u and (v - u) in mass_table.values():
                diff = v - u
                amino_acid = min(a for a, m in mass_table.items() if m == diff)
                graph.setdefault(u, []).append((v, amino_acid))

    target = sorted(spectrum)
    peptide_length = len(target) // 2
    result = [None]

    def dfs(node, peptide):
        if result[0] is not None:
            return
        if node == total:
            if len(peptide) == peptide_length and ideal_spectrum(peptide) == target:
                result[0] = peptide
            return
        for next_node, amino_acid in graph.get(node, []):
            dfs(next_node, peptide + amino_acid)
            if result[0] is not None:
                return

    dfs(0, "")
    return result[0]

spectrum = [0, 57, 57, 154, 154, 211]

print(decode_ideal_spectrum(spectrum))
