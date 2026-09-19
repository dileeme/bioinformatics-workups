def first_occurrence(bwt):
    counts = {}
    for c in bwt:
        counts[c] = counts.get(c, 0) + 1
    first = {}
    total = 0
    for c in sorted(counts):
        first[c] = total
        total += counts[c]
    return first

def last_to_first_mapping(bwt):
    first = first_occurrence(bwt)
    seen = {}
    mapping = [0] * len(bwt)
    for i, c in enumerate(bwt):
        rank = seen.get(c, 0)
        mapping[i] = first[c] + rank
        seen[c] = rank + 1
    return mapping

def bw_matching(bwt, pattern, last_to_first):
    top, bottom = 0, len(bwt) - 1
    remaining = list(pattern)
    while top <= bottom:
        if remaining:
            symbol = remaining.pop()
            positions = [k for k in range(top, bottom + 1) if bwt[k] == symbol]
            if positions:
                top = last_to_first[positions[0]]
                bottom = last_to_first[positions[-1]]
            else:
                return 0
        else:
            return bottom - top + 1
    return 0

bwt = "annb$aa"
patterns = ["ana", "ban"]

last_to_first = last_to_first_mapping(bwt)
counts = [bw_matching(bwt, pattern, last_to_first) for pattern in patterns]
print(" ".join(str(c) for c in counts))
