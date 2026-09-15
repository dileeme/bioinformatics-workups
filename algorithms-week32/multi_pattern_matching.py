def find_all_occurrences(text, patterns):
    positions = set()
    for pattern in patterns:
        start = 0
        while True:
            index = text.find(pattern, start)
            if index == -1:
                break
            positions.add(index)
            start = index + 1
    return sorted(positions)

text = "AATCGGGTTCAATCGGGGT"
patterns = ["ATCG", "GGGT", "TTCA"]

print(" ".join(str(p) for p in find_all_occurrences(text, patterns)))
