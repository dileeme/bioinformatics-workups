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

def closest_motif_match(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + cost, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

    end_i = min(range(n + 1), key=lambda i: dp[i][m])
    best_distance = dp[end_i][m]

    aligned_s, aligned_t = [], []
    i, j = end_i, m
    while j > 0 and i > 0:
        cost = 0 if s[i - 1] == t[j - 1] else 1
        if dp[i][j] == dp[i - 1][j - 1] + cost:
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i][j - 1] + 1:
            aligned_s.append("-")
            aligned_t.append(t[j - 1])
            j -= 1
        else:
            aligned_s.append(s[i - 1])
            aligned_t.append("-")
            i -= 1
    while j > 0:
        aligned_s.append("-")
        aligned_t.append(t[j - 1])
        j -= 1

    return best_distance, "".join(reversed(aligned_s)), "".join(reversed(aligned_t))

fasta = """
>Rosalind_1
ACTGCATATCCATTAGCCTAGCA
>Rosalind_2
CATCA
"""

sequences = parse_fasta(fasta)
s, t = list(sequences.values())

distance, aligned_s, aligned_t = closest_motif_match(s, t)

print(distance)
print(aligned_s)
print(aligned_t)
