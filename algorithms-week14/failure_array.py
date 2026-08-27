def failure_array(s):
    fail = [0] * len(s)
    k = 0
    for i in range(1, len(s)):
        while k > 0 and s[i] != s[k]:
            k = fail[k - 1]
        if s[i] == s[k]:
            k += 1
        fail[i] = k
    return fail

s = "CAGCATGGTATCACAGCAGAG"

print(" ".join(str(n) for n in failure_array(s)))
