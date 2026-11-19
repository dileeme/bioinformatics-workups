def parse_fasta(text):
    sequences = {}
    label = None
    for line in text.strip().splitlines():
        if line.startswith(">"):
            label = line[1:].strip()
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return sequences

def column_score(a, b, c):
    return 0 if a == b == c else -1

def multiple_alignment(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    neg_inf = float("-inf")
    dp = [[[neg_inf] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    back = [[[None] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    dp[0][0][0] = 0

    moves = [
        (1, 1, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1),
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
    ]

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            for k in range(n3 + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                best = neg_inf
                best_move = None
                for di, dj, dk in moves:
                    pi, pj, pk = i - di, j - dj, k - dk
                    if pi < 0 or pj < 0 or pk < 0:
                        continue
                    if dp[pi][pj][pk] == neg_inf:
                        continue
                    a = s1[pi] if di else "-"
                    b = s2[pj] if dj else "-"
                    c = s3[pk] if dk else "-"
                    score = dp[pi][pj][pk] + column_score(a, b, c)
                    if score > best:
                        best = score
                        best_move = (di, dj, dk)
                dp[i][j][k] = best
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

fasta = """
>S1
ATC
>S2
AC
>S3
ATC
"""

sequences = parse_fasta(fasta)
s1, s2, s3 = sequences.values()

score, a1, a2, a3 = multiple_alignment(s1, s2, s3)
print(score)
print(a1)
print(a2)
print(a3)
