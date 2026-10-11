def format_set(s):
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}"

n = 10
A = {1, 2, 3, 4, 5}
B = {2, 8, 5, 10}
universe = set(range(1, n + 1))

print(format_set(A | B))
print(format_set(A & B))
print(format_set(A - B))
print(format_set(B - A))
print(format_set(universe - A))
print(format_set(universe - B))
