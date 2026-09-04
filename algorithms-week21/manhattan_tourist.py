def longest_manhattan_path(n, m, down, right):
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])
    return s[n][m]

n, m = 4, 4

down = [
    [1, 0, 2, 4, 3],
    [4, 6, 5, 2, 1],
    [4, 4, 5, 2, 1],
    [5, 6, 8, 5, 3],
]

right = [
    [3, 2, 4, 0],
    [3, 2, 4, 2],
    [0, 7, 3, 3],
    [3, 3, 0, 2],
    [1, 3, 2, 2],
]

print(longest_manhattan_path(n, m, down, right))
