def partial_permutations(n, k):
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result % 1000000

n = 21
k = 7

print(partial_permutations(n, k))
