def format_set(s):
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}"

n = 10
a = {1, 2, 3, 4, 5}
b = {2, 8, 5, 10}
universe = set(range(1, n + 1))

union = a | b
intersection = a & b
a_minus_b = a - b
b_minus_a = b - a
a_complement = universe - a
b_complement = universe - b

print(format_set(union))
print(format_set(intersection))
print(format_set(a_minus_b))
print(format_set(b_minus_a))
print(format_set(a_complement))
print(format_set(b_complement))
