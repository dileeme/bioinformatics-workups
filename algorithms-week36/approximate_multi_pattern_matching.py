def hamming_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

def approximate_occurrences(text, patterns, max_mismatches):
    positions = set()
    for pattern in patterns:
        length = len(pattern)
        for i in range(len(text) - length + 1):
            if hamming_distance(text[i:i + length], pattern) <= max_mismatches:
                positions.add(i)
    return sorted(positions)

text = "AACCTTGG"
patterns = ["ACCT", "TTGG"]
max_mismatches = 1

positions = approximate_occurrences(text, patterns, max_mismatches)
print(" ".join(str(p + 1) for p in positions))
