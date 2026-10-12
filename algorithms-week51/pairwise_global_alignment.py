MATCH = 5
MISMATCH = -4
GAP_OPEN = 10
GAP_EXTEND = 0.5
NEG_INF = float("-inf")

def substitution_score(a, b):
    return MATCH if a == b else MISMATCH

def global_alignment_score(s, t):
    n, m = len(s), len(t)
    match = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    gap_s = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    gap_t = [[NEG_INF] * (m + 1) for _ in range(n + 1)]

    match[0][0] = 0.0
    for i in range(1, n + 1):
        gap_s[i][0] = -(GAP_OPEN + (i - 1) * GAP_EXTEND)
    for j in range(1, m + 1):
        gap_t[0][j] = -(GAP_OPEN + (j - 1) * GAP_EXTEND)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match[i][j] = substitution_score(s[i - 1], t[j - 1]) + max(
                match[i - 1][j - 1], gap_s[i - 1][j - 1], gap_t[i - 1][j - 1]
            )
            gap_s[i][j] = max(
                match[i - 1][j] - GAP_OPEN,
                gap_s[i - 1][j] - GAP_EXTEND,
                gap_t[i - 1][j] - GAP_OPEN,
            )
            gap_t[i][j] = max(
                match[i][j - 1] - GAP_OPEN,
                gap_s[i][j - 1] - GAP_OPEN,
                gap_t[i][j - 1] - GAP_EXTEND,
            )

    return max(match[n][m], gap_s[n][m], gap_t[n][m])

s = "TATGGCAATTCGCCTAGCGT"
t = "TATTGGCATCGCATAGGCGT"

print(f"{global_alignment_score(s, t):.1f}")
