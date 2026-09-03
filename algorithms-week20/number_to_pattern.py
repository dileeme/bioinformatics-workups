def number_to_pattern(number, k):
    bases = "ACGT"
    pattern = []
    for _ in range(k):
        number, remainder = divmod(number, 4)
        pattern.append(bases[remainder])
    return "".join(reversed(pattern))

number = 45
k = 4

print(number_to_pattern(number, k))
