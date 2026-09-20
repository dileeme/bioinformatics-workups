def longest_multiple_repeat(s, k):
    n = len(s)
    best = ""
    for length in range(n, 0, -1):
        seen = {}
        for i in range(n - length + 1):
            substring = s[i:i + length]
            seen[substring] = seen.get(substring, 0) + 1
        for substring, count in seen.items():
            if count >= k and len(substring) > len(best):
                best = substring
        if best:
            return best
    return best

s = "ATATCGTTTTATCGTT"
k = 3

print(longest_multiple_repeat(s, k))
