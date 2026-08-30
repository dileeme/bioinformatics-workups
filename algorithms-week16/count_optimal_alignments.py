MOD = 134217727

def count_optimal_alignments(s, t):
    n, m = len(s), len(t)
    dist = [[0] * (m + 1) for _ in range(n + 1)]
    count = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][0] = i
        count[i][0] = 1
    for j in range(m + 1):
        dist[0][j] = j
        count[0][j] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dist[i - 1][j - 1] + (0 if s[i - 1] == t[j - 1] else 1)
            up = dist[i - 1][j] + 1
            left = dist[i][j - 1] + 1
            best = min(diag, up, left)
            dist[i][j] = best
            total = 0
            if diag == best:
                total += count[i - 1][j - 1]
            if up == best:
                total += count[i - 1][j]
            if left == best:
                total += count[i][j - 1]
            count[i][j] = total % MOD
    return dist[n][m], count[n][m]

s = "PRETTY"
t = "PRTTEIN"

distance, alignments = count_optimal_alignments(s, t)
print(distance)
print(alignments)
