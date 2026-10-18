NEG_INF = float("-inf")

MASS = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "L": 113, "I": 113, "N": 114, "D": 115, "K": 128, "Q": 128,
    "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

def highest_scoring_modified_peptide(peptide, spectrum, k):
    n = len(peptide)
    m = len(spectrum)
    s = [0] + spectrum
    dp = [[[NEG_INF] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        w = MASS[peptide[i - 1]]
        best_prev = [max((dp[i - 1][j][t] for j in range(m + 1)), default=NEG_INF) for t in range(k + 1)]
        for j in range(m + 1):
            for t in range(k + 1):
                best = NEG_INF
                if j - w >= 0 and dp[i - 1][j - w][t] > NEG_INF:
                    best = max(best, dp[i - 1][j - w][t] + s[j])
                if t >= 1 and best_prev[t - 1] > NEG_INF:
                    best = max(best, best_prev[t - 1] + s[j])
                dp[i][j][t] = best

    return max(dp[n][m][t] for t in range(k + 1))

peptide = "GAG"
spectrum = [7, -2, -3, 8, 1, 0, 0, -1, 8, -2, 7, 8, 5, -2, 6, 3, -3, -3, -2, 0, 0, 5, 6, -3, 5, 0, 8, 7,
            8, 5, 3, 0, 4, 6, 1, 9, -3, 9, 9, -1, 8, 3, 2, 1, -1, 0, 9, 2, -2, -2, 3, -2, 2, 2, 6, 1, 9,
            -3, 8, 4, 5, -2, 3, -2, 5, 1, 7, 6, 2, 6, 0, 8, -2, -3, 7, 0, 9, 1, -2, 0, -2, 3, 1, 4, 7, 2,
            -1, 2, 2, 0, 7, 1, 8, 7, 7, -2, 6, 7, -1, 5, 8, 0, -1, 4, 3, 1, 7, 8, 5, 0, 7, 2, 9, 9, -3,
            0, -3, 9, 2, 3, 1, -2, 0, 6, 8, 2, 0, 7, 4, 3, 7, 4, -1, 1, -1, 0, 8, 5, 5, 1, 8, 6, 3, 6, 3,
            2, 0, -1, 5, 4, -2, 9, -3, -2, -1, 7, -1, 9, 7, 3, 6, -2, 3, 3, 6, 4, 5, 1, 5, -3, 7, 8, -2,
            7, 5, 9, 1, 9, 7, 2, -2, 1, 3, -1, 4, -3, 8, 8, 1, 5]
k = 1

print(highest_scoring_modified_peptide(peptide, spectrum, k))
