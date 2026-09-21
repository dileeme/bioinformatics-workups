NEG_INF = float("-inf")

def parse_fasta(text):
    sequences = {}
    label = None
    for line in text.strip().splitlines():
        if line.startswith(">"):
            label = line[1:].strip()
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return sequences

def score(a, b, match=5, mismatch=-4):
    return match if a == b else mismatch

def global_alignment_affine_gap(s, t, gap_open=10, gap_extend=1):
    n, m = len(s), len(t)
    match_matrix = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    gap_s = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    gap_t = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    match_matrix[0][0] = 0

    for i in range(1, n + 1):
        gap_s[i][0] = -gap_open - (i - 1) * gap_extend
    for j in range(1, m + 1):
        gap_t[0][j] = -gap_open - (j - 1) * gap_extend

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            best_diag = max(match_matrix[i - 1][j - 1], gap_s[i - 1][j - 1], gap_t[i - 1][j - 1])
            match_matrix[i][j] = best_diag + score(s[i - 1], t[j - 1])
            gap_s[i][j] = max(match_matrix[i - 1][j] - gap_open, gap_s[i - 1][j] - gap_extend)
            gap_t[i][j] = max(match_matrix[i][j - 1] - gap_open, gap_t[i][j - 1] - gap_extend)

    return max(match_matrix[n][m], gap_s[n][m], gap_t[n][m])

fasta = """
>Rosalind_1
GATTACAGATTACA
>Rosalind_2
GCATGCTGATCA
"""

sequences = parse_fasta(fasta)
s, t = list(sequences.values())

print(global_alignment_affine_gap(s, t))
