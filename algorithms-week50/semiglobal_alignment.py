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

def semiglobal_alignment(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = 1 if s[i - 1] == t[j - 1] else -1
            dp[i][j] = max(dp[i - 1][j - 1] + match_score, dp[i - 1][j] - 1, dp[i][j - 1] - 1)

    best_score = dp[n][m]
    end_i, end_j = n, m
    for i in range(n + 1):
        if dp[i][m] > best_score:
            best_score = dp[i][m]
            end_i, end_j = i, m
    for j in range(m + 1):
        if dp[n][j] > best_score:
            best_score = dp[n][j]
            end_i, end_j = n, j

    aligned_s, aligned_t = [], []
    i, j = end_i, end_j
    while i > 0 and j > 0:
        match_score = 1 if s[i - 1] == t[j - 1] else -1
        if dp[i][j] == dp[i - 1][j - 1] + match_score:
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] - 1:
            aligned_s.append(s[i - 1])
            aligned_t.append("-")
            i -= 1
        else:
            aligned_s.append("-")
            aligned_t.append(t[j - 1])
            j -= 1

    prefix_s, prefix_t = s[:i], t[:j]
    aligned_s = list(prefix_s) + [""] * (len(prefix_t) - len(prefix_s)) + list(reversed(aligned_s))
    aligned_t = [""] * (len(prefix_s) - len(prefix_t)) + list(prefix_t) + list(reversed(aligned_t))

    suffix_s, suffix_t = s[end_i:], t[end_j:]
    aligned_s += list(suffix_s) + [""] * (len(suffix_t) - len(suffix_s))
    aligned_t += [""] * (len(suffix_s) - len(suffix_t)) + list(suffix_t)

    aligned_s = [c if c != "" else "-" for c in aligned_s]
    aligned_t = [c if c != "" else "-" for c in aligned_t]

    return best_score, "".join(aligned_s), "".join(aligned_t)

fasta = """
>Rosalind_12
CAGCACTTGGATTCTCGG
>Rosalind_14
CAGCGTGG
"""

sequences = parse_fasta(fasta)
s, t = list(sequences.values())

score, aligned_s, aligned_t = semiglobal_alignment(s, t)

print(score)
print(aligned_s)
print(aligned_t)
