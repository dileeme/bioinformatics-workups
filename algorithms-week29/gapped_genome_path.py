def string_spelled_by_gapped_patterns(pairs, k, d):
    prefixes = [p for p, _ in pairs]
    suffixes = [s for _, s in pairs]

    prefix_string = prefixes[0]
    for prefix in prefixes[1:]:
        prefix_string += prefix[-1]

    suffix_string = suffixes[0]
    for suffix in suffixes[1:]:
        suffix_string += suffix[-1]

    overlap = len(prefix_string) - (k + d)
    if prefix_string[k + d:] != suffix_string[:overlap]:
        return None

    return prefix_string + suffix_string[overlap:]

k = 4
d = 2
pairs = [
    ("GACC", "GCGC"),
    ("ACCG", "CGCC"),
    ("CCGA", "GCCG"),
    ("CGAG", "CCGG"),
    ("GAGC", "CGGA"),
]

print(string_spelled_by_gapped_patterns(pairs, k, d))
