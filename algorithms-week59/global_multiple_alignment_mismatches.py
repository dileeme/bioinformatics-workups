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

def global_alignment(s, t, match=1, mismatch=-1, gap=-2):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i * gap
    for j in range(1, m + 1):
        dp[0][j] = j * gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i - 1][j - 1] + (match if s[i - 1] == t[j - 1] else mismatch)
            up = dp[i - 1][j] + gap
            left = dp[i][j - 1] + gap
            dp[i][j] = max(diag, up, left)

    aligned_s, aligned_t = [], []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (match if s[i - 1] == t[j - 1] else mismatch):
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + gap:
            aligned_s.append(s[i - 1])
            aligned_t.append("-")
            i -= 1
        else:
            aligned_s.append("-")
            aligned_t.append(t[j - 1])
            j -= 1

    return "".join(reversed(aligned_s)), "".join(reversed(aligned_t))

def merge_alignments(ref_a, other_a, ref_b, other_b):
    merged_ref, merged_a, merged_b = [], [], []
    i = j = 0
    while i < len(ref_a) or j < len(ref_b):
        c1 = ref_a[i] if i < len(ref_a) else None
        c2 = ref_b[j] if j < len(ref_b) else None
        if c1 == "-" and c2 != "-":
            merged_ref.append("-")
            merged_a.append(other_a[i])
            merged_b.append("-")
            i += 1
        elif c2 == "-" and c1 != "-":
            merged_ref.append("-")
            merged_a.append("-")
            merged_b.append(other_b[j])
            j += 1
        elif c1 == "-" and c2 == "-":
            merged_ref.append("-")
            merged_a.append(other_a[i])
            merged_b.append(other_b[j])
            i += 1
            j += 1
        else:
            merged_ref.append(c1)
            merged_a.append(other_a[i])
            merged_b.append(other_b[j])
            i += 1
            j += 1
    return "".join(merged_ref), "".join(merged_a), "".join(merged_b)

def count_mismatched_columns(seq1, seq2, seq3):
    ref_a, aligned_2 = global_alignment(seq1, seq2)
    ref_b, aligned_3 = global_alignment(seq1, seq3)
    merged_ref, merged_2, merged_3 = merge_alignments(ref_a, aligned_2, ref_b, aligned_3)
    return sum(1 for a, b, c in zip(merged_ref, merged_2, merged_3) if not (a == b == c))

fasta = """
>Rosalind_1
MPRTEINSAMPLEKQ
>Rosalind_2
MPRTDINSAMPLEKQ
>Rosalind_3
MPRTEINAMPLEKR
"""

sequences = parse_fasta(fasta)
seq1, seq2, seq3 = sequences.values()

print(count_mismatched_columns(seq1, seq2, seq3))
