from itertools import permutations, product

def signed_permutations(n):
    results = []
    for perm in permutations(range(1, n + 1)):
        for signs in product([1, -1], repeat=n):
            results.append([value * sign for value, sign in zip(perm, signs)])
    return results

n = 2

permutations_list = signed_permutations(n)

print(len(permutations_list))
for perm in permutations_list:
    print(" ".join(map(str, perm)))
