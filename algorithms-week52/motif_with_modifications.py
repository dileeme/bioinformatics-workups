def find_motif_with_modifications(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[None] * (m + 1) for _ in range(n + 1)]

    for j in range(1, m + 1):
        dp[0][j] = j
        backtrack[0][j] = "left"

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i - 1][j - 1] + (0 if s[i - 1] == t[j - 1] else 1)
            up = dp[i - 1][j] + 1
            left = dp[i][j - 1] + 1
            best = min(diag, up, left)
            dp[i][j] = best
            if best == diag:
                backtrack[i][j] = "diag"
            elif best == up:
                backtrack[i][j] = "up"
            else:
                backtrack[i][j] = "left"

    best_i = min(range(n + 1), key=lambda i: dp[i][m])
    best_distance = dp[best_i][m]

    i, j = best_i, m
    aligned_s, aligned_t = [], []
    while j > 0:
        move = backtrack[i][j]
        if move == "diag":
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i, j = i - 1, j - 1
        elif move == "up":
            aligned_s.append(s[i - 1])
            aligned_t.append("-")
            i, j = i - 1, j
        else:
            aligned_s.append("-")
            aligned_t.append(t[j - 1])
            i, j = i, j - 1

    aligned_s.reverse()
    aligned_t.reverse()
    return best_distance, "".join(aligned_s), "".join(aligned_t)

s = "GCCAACAGGGTTTGCGTACGTACCATATAGCTCCGAACTCGTACTCTGCG"
t = "GCGTATCT"

distance, aligned_s, aligned_t = find_motif_with_modifications(s, t)
print(distance)
print(aligned_s)
print(aligned_t)
