def dnafull_matrix():
    bases = "ACGT"
    matrix = {}
    for a in bases:
        matrix[a] = {}
        for b in bases:
            matrix[a][b] = 5 if a == b else -4
    return matrix

def global_alignment_score(s, t, matrix, gap_open=10, gap_extend=1):
    n, m = len(s), len(t)
    neg_inf = float("-inf")
    match = [[neg_inf] * (m + 1) for _ in range(n + 1)]
    gap_t = [[neg_inf] * (m + 1) for _ in range(n + 1)]
    gap_s = [[neg_inf] * (m + 1) for _ in range(n + 1)]
    match[0][0] = 0
    for i in range(1, n + 1):
        gap_t[i][0] = -gap_open - (i - 1) * gap_extend
    for j in range(1, m + 1):
        gap_s[0][j] = -gap_open - (j - 1) * gap_extend

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score = matrix[s[i - 1]][t[j - 1]]
            match[i][j] = max(match[i - 1][j - 1], gap_t[i - 1][j - 1], gap_s[i - 1][j - 1]) + score
            gap_t[i][j] = max(match[i - 1][j] - gap_open, gap_t[i - 1][j] - gap_extend)
            gap_s[i][j] = max(match[i][j - 1] - gap_open, gap_s[i][j - 1] - gap_extend)

    return max(match[n][m], gap_t[n][m], gap_s[n][m])

seq1 = "TATTACGAGGGCCAGCTCTCCTTAATTGTACGGGCTATAAACTCGGGCCCTCGTTCTTACCAGCTAGTGTA"
seq2 = "TATAACGAGAGCCCGCTCCCTTAATTTGTACGGGTTATAACCTCGGACCCTCGTTCCTTTCCAGCTAGTA"

matrix = dnafull_matrix()

print(global_alignment_score(seq1, seq2, matrix))
