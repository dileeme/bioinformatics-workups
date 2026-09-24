def word_counts(s):
    counts = {}
    for word in s.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

s = "We tried list and we tried dicts also we tried Zen"

for word, count in word_counts(s).items():
    print(word, count)
