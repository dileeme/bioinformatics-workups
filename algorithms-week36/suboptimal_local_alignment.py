def hamming_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

def suboptimal_alignment(s, t, min_len=32, max_mismatches=3):
    best_len, best_i, best_j = 0, -1, -1
    for i in range(len(s) - min_len + 1):
        for j in range(len(t) - min_len + 1):
            if hamming_distance(s[i:i + min_len], t[j:j + min_len]) > max_mismatches:
                continue
            length = min_len
            mismatches = hamming_distance(s[i:i + min_len], t[j:j + min_len])
            while i + length < len(s) and j + length < len(t):
                if s[i + length] != t[j + length]:
                    if mismatches + 1 > max_mismatches:
                        break
                    mismatches += 1
                length += 1
            if length > best_len:
                best_len, best_i, best_j = length, i, j
    return best_len, best_i + 1, best_j + 1

s = "TTTT" + "ACGTACGTACGTACGTACGTACGTACGTACGT" + "TTTT"
t = "GGGG" + "ACGTAGGTACGTACGAACGTACGTATGTACGT" + "GGGG"

length, s_start, t_start = suboptimal_alignment(s, t)
print(length)
print(s_start)
print(t_start)
