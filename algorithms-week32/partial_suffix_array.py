def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

def partial_suffix_array(s, k):
    sa = suffix_array(s)
    return [(i, value) for i, value in enumerate(sa) if value % k == 0]

s = "PANAMABANANAS$"
k = 5

for i, value in partial_suffix_array(s, k):
    print(f"{i},{value}")
