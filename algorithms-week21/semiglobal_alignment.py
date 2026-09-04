def semiglobal_alignment(s, t, match=1, mismatch=-1, gap=-1):
    n, m = len(s), len(t)
    score = [[0] * (m + 1) for _ in range(n + 1)]
    trace = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        trace[i][0] = "up"
    for j in range(1, m + 1):
        trace[0][j] = "left"

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = score[i - 1][j - 1] + (match if s[i - 1] == t[j - 1] else mismatch)
            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            best = max(diag, up, left)
            score[i][j] = best
            trace[i][j] = "diag" if best == diag else ("up" if best == up else "left")

    best_score, best_i, best_j = max(
        (score[n][j], n, j) for j in range(m + 1)
    )
    for i in range(n + 1):
        if score[i][m] > best_score:
            best_score, best_i, best_j = score[i][m], i, m

    aligned_s, aligned_t = [], []
    i, j = best_i, best_j
    for k in range(n, best_i, -1):
        aligned_s.append(s[k - 1])
        aligned_t.append("-")
    for k in range(m, best_j, -1):
        aligned_s.append("-")
        aligned_t.append(t[k - 1])

    while i > 0 and j > 0:
        direction = trace[i][j]
        if direction == "diag":
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif direction == "up":
            aligned_s.append(s[i - 1])
            aligned_t.append("-")
            i -= 1
        else:
            aligned_s.append("-")
            aligned_t.append(t[j - 1])
            j -= 1

    while i > 0:
        aligned_s.append(s[i - 1])
        aligned_t.append("-")
        i -= 1
    while j > 0:
        aligned_s.append("-")
        aligned_t.append(t[j - 1])
        j -= 1

    aligned_s.reverse()
    aligned_t.reverse()
    return best_score, "".join(aligned_s), "".join(aligned_t)

s = "AGCTAGCT"
t = "GCTAGC"

best_score, aligned_s, aligned_t = semiglobal_alignment(s, t)
print(best_score)
print(aligned_s)
print(aligned_t)
