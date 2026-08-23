from itertools import permutations
from math import factorial

def enumerate_permutations(n):
    return list(permutations(range(1, n + 1)))

n = 3

perms = enumerate_permutations(n)
print(factorial(n))
for perm in perms:
    print(" ".join(str(x) for x in perm))
