def ordered_strings(alphabet, max_length):
    rank = {c: i for i, c in enumerate(alphabet)}
    words = []
    for length in range(1, max_length + 1):
        words.extend(_combos(alphabet, length))
    words.sort(key=lambda w: tuple(rank[c] for c in w))
    return words

def _combos(alphabet, length):
    if length == 0:
        return [""]
    smaller = _combos(alphabet, length - 1)
    return [c + w for c in alphabet for w in smaller]

alphabet = ["D", "N"]
max_length = 3

for word in ordered_strings(alphabet, max_length):
    print(word)
