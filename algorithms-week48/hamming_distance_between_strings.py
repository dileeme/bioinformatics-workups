def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

s = "GGGCCGTTGGT"
t = "GGACCGTTGAC"

print(hamming_distance(s, t))
