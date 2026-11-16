def tree_height(parents):
    n = len(parents)
    depth = [-1] * n

    def get_depth(i):
        if depth[i] != -1:
            return depth[i]
        if parents[i] == -1:
            depth[i] = 0
        else:
            depth[i] = get_depth(parents[i] - 1) + 1
        return depth[i]

    for i in range(n):
        get_depth(i)
    return max(depth)

parents = [-1, 1, 1, 2, 2]

print(tree_height(parents))
