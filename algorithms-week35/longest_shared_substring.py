def suffix_array(text):
    return sorted(range(len(text)), key=lambda i: text[i:])

def lcp(a, b):
    length = 0
    while length < len(a) and length < len(b) and a[length] == b[length]:
        length += 1
    return length

def longest_shared_substring(s, t):
    combined = s + "#" + t + "$"
    order = suffix_array(combined)

    best_length = 0
    best_start = 0
    for k in range(len(order) - 1):
        i, j = order[k], order[k + 1]
        if (i < len(s)) != (j < len(s)):
            length = lcp(combined[i:], combined[j:])
            if length > best_length:
                best_length = length
                best_start = i

    return combined[best_start:best_start + best_length]

s = "ABCXYZDEF"
t = "QQXYZDRST"

print(longest_shared_substring(s, t))
