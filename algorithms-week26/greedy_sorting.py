def greedy_sorting(permutation):
    perm = list(permutation)
    n = len(perm)
    steps = []

    for i in range(n):
        if abs(perm[i]) != i + 1:
            j = next(k for k in range(i, n) if abs(perm[k]) == i + 1)
            perm[i:j + 1] = [-x for x in reversed(perm[i:j + 1])]
            steps.append(list(perm))
        if perm[i] == -(i + 1):
            perm[i] = i + 1
            steps.append(list(perm))

    return steps

def format_permutation(perm):
    return " ".join(f"+{x}" if x > 0 else str(x) for x in perm)

permutation = [-3, 4, 1, 5, -2]

for step in greedy_sorting(permutation):
    print(format_permutation(step))
