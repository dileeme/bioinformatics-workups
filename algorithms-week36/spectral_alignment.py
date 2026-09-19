integer_mass = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128,
    "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
}

def spectral_alignment(peptide, spectral_vector, k):
    n = len(peptide)
    m = len(spectral_vector)
    neg_inf = float("-inf")
    dp = [[[neg_inf] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    back = [[[None] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        mass = integer_mass[peptide[i - 1]]
        for j in range(m + 1):
            gain = spectral_vector[j - 1] if j >= 1 else 0
            for t in range(k + 1):
                best, choice = neg_inf, None
                unmodified = j - mass
                if unmodified >= 0 and dp[i - 1][unmodified][t] != neg_inf:
                    best, choice = dp[i - 1][unmodified][t] + gain, ("diag", unmodified)
                if t >= 1:
                    for prev in range(m + 1):
                        if dp[i - 1][prev][t - 1] != neg_inf:
                            val = dp[i - 1][prev][t - 1] + gain
                            if val > best:
                                best, choice = val, ("mod", prev)
                dp[i][j][t] = best
                back[i][j][t] = choice

    best_t = max(range(k + 1), key=lambda t: dp[n][m][t])
    modifications = [0] * n
    i, j, t = n, m, best_t
    while i > 0:
        kind, prev = back[i][j][t]
        mass = integer_mass[peptide[i - 1]]
        if kind == "diag":
            modifications[i - 1] = 0
        else:
            modifications[i - 1] = (j - prev) - mass
            t -= 1
        j = prev
        i -= 1

    return dp[n][m][best_t], modifications

peptide = "GA"
spectral_vector = [-5] * 130
spectral_vector[58] = 100
spectral_vector[129] = 100
k = 1

score, modifications = spectral_alignment(peptide, spectral_vector, k)
print(score)
print(" ".join(str(d) for d in modifications))
