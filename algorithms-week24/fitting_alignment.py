def fitting_alignment(s, t, match=1, mismatch=-1, gap=-1):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[None] * (m + 1) for _ in range(n + 1)]

    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + gap
        backtrack[0][j] = "left"

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i - 1][j - 1] + (match if s[i - 1] == t[j - 1] else mismatch)
            up = dp[i - 1][j] + gap
            left = dp[i][j - 1] + gap
            best = max(diag, up, left)
            dp[i][j] = best
            if best == diag:
                backtrack[i][j] = "diag"
            elif best == up:
                backtrack[i][j] = "up"
            else:
                backtrack[i][j] = "left"

    best_i = max(range(n + 1), key=lambda i: dp[i][m])
    best_score = dp[best_i][m]

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
    return best_score, "".join(aligned_s), "".join(aligned_t)

s = "GTAGGCTTAAGGTTA"
t = "TAGATA"

score, aligned_s, aligned_t = fitting_alignment(s, t)
print(score)
print(aligned_s)
print(aligned_t)
