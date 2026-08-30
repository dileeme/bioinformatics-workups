def is_interleaving(t1, t2, window):
    len1, len2 = len(t1), len(t2)
    if len1 + len2 != len(window):
        return False
    dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
    dp[0][0] = True
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 and j == 0:
                continue
            ok = False
            if i > 0 and dp[i - 1][j] and t1[i - 1] == window[i + j - 1]:
                ok = True
            if not ok and j > 0 and dp[i][j - 1] and t2[j - 1] == window[i + j - 1]:
                ok = True
            dp[i][j] = ok
    return dp[len1][len2]

def occurs_as_interleaving(s, t1, t2):
    window_len = len(t1) + len(t2)
    for start in range(len(s) - window_len + 1):
        window = s[start:start + window_len]
        if is_interleaving(t1, t2, window):
            return True
    return False

def disjoint_motif_matrix(s, motifs):
    n = len(motifs)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if occurs_as_interleaving(s, motifs[i], motifs[j]):
                matrix[i][j] = 1
    return matrix

s = "ACGTAGCTAGCGATCGA"
motifs = ["AG", "GC", "GAT"]

matrix = disjoint_motif_matrix(s, motifs)
for row in matrix:
    print(" ".join(str(v) for v in row))
