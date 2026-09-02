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

def overlap_alignment(s, t, match=1, mismatch=-2, gap=-2):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score = match if s[i - 1] == t[j - 1] else mismatch
            dp[i][j] = max(dp[i - 1][j - 1] + score, dp[i - 1][j] + gap, dp[i][j - 1] + gap)

    best_j = max(range(m + 1), key=lambda j: dp[n][j])
    best_score = dp[n][best_j]

    aligned_s, aligned_t = [], []
    i, j = n, best_j
    while i > 0 and j > 0:
        score = match if s[i - 1] == t[j - 1] else mismatch
        if dp[i][j] == dp[i - 1][j - 1] + score:
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + gap:
            aligned_s.append(s[i - 1])
            aligned_t.append("-")
            i -= 1
        else:
            aligned_s.append("-")
            aligned_t.append(t[j - 1])
            j -= 1

    return best_score, "".join(reversed(aligned_s)), "".join(reversed(aligned_t))

fasta = """
>Rosalind_1
GATTACAGGC
>Rosalind_2
TACAGATCCA
"""

sequences = parse_fasta(fasta)
s, t = list(sequences.values())

score, aligned_s, aligned_t = overlap_alignment(s, t)

print(score)
print(aligned_s)
print(aligned_t)
