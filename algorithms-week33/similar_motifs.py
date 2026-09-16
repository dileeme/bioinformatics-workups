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
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[n][m]

def find_similar_motifs(s, t, k):
    n, m = len(s), len(t)
    min_len = max(1, m - k)
    max_len = min(n, m + k)
    results = []
    for length in range(min_len, max_len + 1):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if edit_distance(substring, t) <= k:
                results.append((start + 1, start + length, substring))
    return results

s = "ACGTAGCATCGACTGCATCG"
t = "CATCG"
k = 1

for start, end, substring in find_similar_motifs(s, t, k):
    print(start, end, substring)
