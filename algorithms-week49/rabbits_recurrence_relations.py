def rabbit_pairs(n, k):
    if n <= 2:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + k * prev2
    return prev1

n = 5
k = 3

print(rabbit_pairs(n, k))
