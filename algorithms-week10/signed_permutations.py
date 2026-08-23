from itertools import permutations, product
from math import factorial

def enumerate_signed_permutations(n):
    results = []
    for perm in permutations(range(1, n + 1)):
        for signs in product([1, -1], repeat=n):
            results.append([x * s for x, s in zip(perm, signs)])
    return results

n = 1

signed_perms = enumerate_signed_permutations(n)
print(factorial(n) * 2 ** n)
for perm in signed_perms:
    print(" ".join(str(x) for x in perm))
