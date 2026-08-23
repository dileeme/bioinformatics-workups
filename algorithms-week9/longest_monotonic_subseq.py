def longest_increasing_subsequence(perm):
    n = len(perm)
    lengths = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if perm[j] < perm[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                prev[i] = j

    best = max(range(n), key=lambda i: lengths[i])
    subseq = []
    while best != -1:
        subseq.append(perm[best])
        best = prev[best]
    return subseq[::-1]

perm = [5, 1, 4, 2, 3]

increasing = longest_increasing_subsequence(perm)
decreasing = [-x for x in longest_increasing_subsequence([-x for x in perm])]

print(" ".join(str(x) for x in increasing))
print(" ".join(str(x) for x in decreasing))
