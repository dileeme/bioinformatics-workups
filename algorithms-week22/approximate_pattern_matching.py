def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

def approximate_occurrences(pattern, text, d):
    k = len(pattern)
    positions = []
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i:i + k]) <= d:
            positions.append(i)
    return positions

pattern = "GATT"
text = "GATTACAGATCGATTTAAC"
d = 1

print(" ".join(str(p) for p in approximate_occurrences(pattern, text, d)))
