def find_maximal_repeats(s, min_len):
    n = len(s)
    results = set()
    for length in range(min_len, n):
        occurrences = {}
        for i in range(n - length + 1):
            occurrences.setdefault(s[i:i + length], []).append(i)
        for word, starts in occurrences.items():
            if len(starts) < 2:
                continue
            left_chars = {s[i - 1] if i > 0 else None for i in starts}
            if len(left_chars) <= 1:
                continue
            right_chars = {s[i + length] if i + length < n else None for i in starts}
            if len(right_chars) <= 1:
                continue
            results.add(word)
    return results

s = "CCGAATAGGGAAGCCCAATAAACCACTCTGACTGGCGACATGTGCATATAGGCAAAAGCCCAATAAACCACTCTGACTGGGGCGACCCTT"

for repeat in sorted(find_maximal_repeats(s, 20)):
    print(repeat)
