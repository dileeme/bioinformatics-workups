def spectral_convolution(s1, s2):
    differences = {}
    for a in s1:
        for b in s2:
            diff = round(a - b, 5)
            differences[diff] = differences.get(diff, 0) + 1

    best_diff = max(differences, key=lambda d: differences[d])
    return differences[best_diff], best_diff

s1 = [-10, -8, -5, 2, 3]
s2 = [-11, -8, -3, 2, 3]

multiplicity, value = spectral_convolution(s1, s2)
print(multiplicity)
print(value)
