def two_sum(arr):
    seen = {}
    for i, value in enumerate(arr):
        complement = -value
        if complement in seen:
            return (seen[complement] + 1, i + 1)
        if value not in seen:
            seen[value] = i
    return None

arrays = [
    [2, -3, 4, 10, -4, 5],
    [1, 2, 3, 4, 5, 6],
    [-5, -4, -3, -2, -1, 5],
]

for arr in arrays:
    result = two_sum(arr)
    print(" ".join(str(x) for x in result) if result else -1)
