def rabbit_pairs(n, k):
    prev, curr = 1, 1
    for _ in range(n - 2):
        prev, curr = curr, curr + k * prev
    return curr

n = 5
k = 3

print(rabbit_pairs(n, k))
