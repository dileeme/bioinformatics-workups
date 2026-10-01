def kmer_substrings(text, k):
    return sorted(text[i:i + k] for i in range(len(text) - k + 1))

k = 5
text = "CAATCCAAC"

for kmer in kmer_substrings(text, k):
    print(kmer)
