from itertools import product

def pattern_to_number(pattern):
    order = {"A": 0, "C": 1, "G": 2, "T": 3}
    number = 0
    for base in pattern:
        number = number * 4 + order[base]
    return number

def frequency_array(text, k):
    counts = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        counts[pattern_to_number(text[i:i + k])] += 1
    return counts

text = "ACGCGGCTCTGAAA"
k = 2

print(" ".join(str(c) for c in frequency_array(text, k)))
