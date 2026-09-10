def limb_length(n, j, matrix):
    best = None
    for i in range(n):
        if i == j:
            continue
        for k in range(n):
            if k == j or k == i:
                continue
            value = (matrix[i][j] + matrix[j][k] - matrix[i][k]) // 2
            if best is None or value < best:
                best = value
    return best

n = 4
j = 1
matrix = [
    [0, 13, 21, 22],
    [13, 0, 12, 13],
    [21, 12, 0, 13],
    [22, 13, 13, 0],
]

print(limb_length(n, j, matrix))
