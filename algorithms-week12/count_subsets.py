def count_subsets(n, modulus=1000000):
    return pow(2, n, modulus)

n = 45

print(count_subsets(n))
