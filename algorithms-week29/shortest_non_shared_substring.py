def substrings_of_length(text, length):
    return {text[i:i + length] for i in range(len(text) - length + 1)}

def shortest_non_shared_substring(text1, text2):
    for length in range(1, len(text1) + 1):
        candidates = substrings_of_length(text1, length)
        other = substrings_of_length(text2, length)
        missing = candidates - other
        if missing:
            return min(missing)
    return None

text1 = "CCAAGCTGCTAGAGG"
text2 = "CATGCTGGGCTGGCT"

print(shortest_non_shared_substring(text1, text2))
