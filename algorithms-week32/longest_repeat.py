def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

def lcp(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i

def longest_repeat(s):
    sa = suffix_array(s)
    best_len, best_start = 0, 0
    for i in range(1, len(sa)):
        length = lcp(s[sa[i - 1]:], s[sa[i]:])
        if length > best_len:
            best_len = length
            best_start = sa[i]
    return s[best_start:best_start + best_len]

s = "ATATCGTTTTATCGTT"

print(longest_repeat(s))
