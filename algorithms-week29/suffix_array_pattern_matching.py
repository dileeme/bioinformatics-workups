def build_suffix_array(text):
    return sorted(range(len(text)), key=lambda i: text[i:])

def pattern_match_range(text, suffix_array, pattern):
    lo, hi = 0, len(suffix_array)
    while lo < hi:
        mid = (lo + hi) // 2
        if text[suffix_array[mid]:suffix_array[mid] + len(pattern)] < pattern:
            lo = mid + 1
        else:
            hi = mid
    start = lo

    hi = len(suffix_array)
    while lo < hi:
        mid = (lo + hi) // 2
        if text[suffix_array[mid]:suffix_array[mid] + len(pattern)].startswith(pattern):
            lo = mid + 1
        else:
            hi = mid
    end = lo

    return suffix_array[start:end]

def match_patterns(text, patterns):
    suffix_array = build_suffix_array(text)
    positions = set()
    for pattern in patterns:
        positions.update(pattern_match_range(text, suffix_array, pattern))
    return sorted(positions)

text = "AATCGGGTTCAATCGGGGT"
patterns = ["CGGG", "AATCG"]

print(" ".join(str(p) for p in match_patterns(text, patterns)))
