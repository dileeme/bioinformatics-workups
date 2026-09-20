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

def score(a, b):
    return 1 if a == b else -1

def global_dp(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] - 1
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] - 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(
                dp[i - 1][j - 1] + score(s1[i - 1], s2[j - 1]),
                dp[i - 1][j] - 1,
                dp[i][j - 1] - 1,
            )
    return dp

def isolate_symbols(s1, s2):
    n, m = len(s1), len(s2)
    prefix_scores = global_dp(s1, s2)
    suffix_scores = global_dp(s1[::-1], s2[::-1])
    best = None
    total = 0
    for i in range(n):
        for j in range(m):
            value = prefix_scores[i][j] + score(s1[i], s2[j]) + suffix_scores[n - 1 - i][m - 1 - j]
            total += value
            if best is None or value > best:
                best = value
    return best, total

fasta = """
>Rosalind_23
GACT
>Rosalind_47
GATC
"""

sequences = parse_fasta(fasta)
s1, s2 = list(sequences.values())

best, total = isolate_symbols(s1, s2)
print(best)
print(total)
