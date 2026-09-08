def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

s = "banana$"

print(" ".join(str(i) for i in suffix_array(s)))
