def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j - 1] + cost,
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
            )
    return dp[n][m]

def find_all_similar_motifs(k, s, t):
    matches = []
    n = len(t)
    for start in range(n):
        for end in range(start + 1, n + 1):
            if abs((end - start) - len(s)) > k:
                continue
            if edit_distance(s, t[start:end]) <= k:
                matches.append((start + 1, end - start))
    return matches

k = 2
s = "ATAT"
t = "GATATCCAT"

for start, length in find_all_similar_motifs(k, s, t):
    print(start, length)
