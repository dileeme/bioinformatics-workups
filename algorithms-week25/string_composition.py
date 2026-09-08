def string_composition(text, k):
    return sorted(text[i:i + k] for i in range(len(text) - k + 1))

text = "CAATCCAAC"
k = 5

for kmer in string_composition(text, k):
    print(kmer)
