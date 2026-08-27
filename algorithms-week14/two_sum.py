def two_sum(a):
    seen = {}
    for j, value in enumerate(a):
        if -value in seen:
            return seen[-value] + 1, j + 1
        seen[value] = j
    return None

datasets = [
    [2, -3, 4, 10, 3],
    [5, -2, 3, -10, 10],
    [8, 3, -6, 4],
]

for a in datasets:
    result = two_sum(a)
    if result:
        print(result[0], result[1])
    else:
        print(-1)
