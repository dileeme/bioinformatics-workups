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

def lcs_length(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

def max_gap_symbols(s, t):
    return len(s) + len(t) - 2 * lcs_length(s, t)

fasta = """
>Rosalind_92
AACGTA
>Rosalind_47
ACACCTA
"""

sequences = parse_fasta(fasta)
s, t = sequences.values()

print(max_gap_symbols(s, t))
