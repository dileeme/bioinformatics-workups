def shortest_common_supersequence(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            result.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            result.append(s[i - 1])
            i -= 1
        else:
            result.append(t[j - 1])
            j -= 1
    while i > 0:
        result.append(s[i - 1])
        i -= 1
    while j > 0:
        result.append(t[j - 1])
        j -= 1

    return "".join(reversed(result))

s = "ATCTGAT"
t = "TGCATA"

print(shortest_common_supersequence(s, t))
