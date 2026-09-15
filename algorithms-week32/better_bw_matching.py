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

def count_matrix(bwt):
    symbols = sorted(set(bwt))
    counts = {c: [0] * (len(bwt) + 1) for c in symbols}
    for i, c in enumerate(bwt):
        for s in symbols:
            counts[s][i + 1] = counts[s][i] + (1 if c == s else 0)
    return counts

def better_bw_matching(bwt, pattern, first, counts):
    top, bottom = 0, len(bwt) - 1
    remaining = list(pattern)
    while top <= bottom:
        if remaining:
            symbol = remaining.pop()
            if counts[symbol][bottom + 1] - counts[symbol][top] > 0:
                top = first[symbol] + counts[symbol][top]
                bottom = first[symbol] + counts[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1
    return 0

bwt = "AGGGG$TTTTCCCCAAAA"
patterns = ["ATCG", "GATC", "CGAT", "TTTT"]

first = first_occurrence(bwt)
counts = count_matrix(bwt)

results = [better_bw_matching(bwt, p, first, counts) for p in patterns]
print(" ".join(str(r) for r in results))
