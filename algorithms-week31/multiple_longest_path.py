def multiple_longest_path(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    dp = [[[0] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    back = [[[None] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    moves = [
        (1, 1, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1),
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
    ]

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            for k in range(n3 + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                best_score = None
                best_move = None
                for di, dj, dk in moves:
                    if di > i or dj > j or dk > k:
                        continue
                    score = dp[i - di][j - dj][k - dk]
                    if di == 1 and dj == 1 and dk == 1 and s1[i - 1] == s2[j - 1] == s3[k - 1]:
                        score += 1
                    if best_score is None or score > best_score:
                        best_score = score
                        best_move = (di, dj, dk)
                dp[i][j][k] = best_score
                back[i][j][k] = best_move

    aligned1, aligned2, aligned3 = [], [], []
    i, j, k = n1, n2, n3
    while (i, j, k) != (0, 0, 0):
        di, dj, dk = back[i][j][k]
        aligned1.append(s1[i - 1] if di else "-")
        aligned2.append(s2[j - 1] if dj else "-")
        aligned3.append(s3[k - 1] if dk else "-")
        i, j, k = i - di, j - dj, k - dk

    return dp[n1][n2][n3], "".join(reversed(aligned1)), "".join(reversed(aligned2)), "".join(reversed(aligned3))

s1, s2, s3 = "ATC", "AC", "ATC"

score, a1, a2, a3 = multiple_longest_path(s1, s2, s3)
print(score)
print(a1)
print(a2)
print(a3)
