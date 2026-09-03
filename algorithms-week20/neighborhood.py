def neighborhood(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}

    neighborhood_set = set()
    suffix_neighbors = neighborhood(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for base in "ACGT":
                neighborhood_set.add(base + text)
        else:
            neighborhood_set.add(pattern[0] + text)
    return neighborhood_set

def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

pattern = "ACG"
d = 1

print("\n".join(sorted(neighborhood(pattern, d))))
