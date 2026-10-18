def local_alignment(s, t, match=1, mismatch=-3, gap=-4):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    best = (0, 0, 0)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i - 1][j - 1] + (match if s[i - 1] == t[j - 1] else mismatch)
            up = dp[i - 1][j] + gap
            left = dp[i][j - 1] + gap
            dp[i][j] = max(0, diag, up, left)
            if dp[i][j] > best[0]:
                best = (dp[i][j], i, j)

    score, end_i, end_j = best
    i, j = end_i, end_j
    while i > 0 and j > 0 and dp[i][j] > 0:
        diag = dp[i - 1][j - 1] + (match if s[i - 1] == t[j - 1] else mismatch)
        if dp[i][j] == diag:
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + gap:
            i -= 1
        else:
            j -= 1
    return s[i:end_i], t[j:end_j]

def count_occurrences(text, pattern):
    count = 0
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            return count
        count += 1
        start = index + 1

repeat = "ACGTTGCATCGGATTACGCA"
mutated_repeat = "ACGTTGCATCTGATTACGCA"

s = "TTGGC" + repeat + "AAAAAAAA" + repeat + "CCGG"
t = "GGCCT" + repeat + "TTTTTTTT" + mutated_repeat + "TTCC"

r, u = local_alignment(s, t)

print(count_occurrences(s, r), count_occurrences(t, r))
