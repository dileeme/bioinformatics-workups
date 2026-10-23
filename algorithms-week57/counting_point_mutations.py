def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

print(hamming_distance(s, t))
