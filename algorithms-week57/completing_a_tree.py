def count_components(n, edges):
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for a, b in edges:
        union(a, b)

    return len({find(node) for node in range(1, n + 1)})

n = 10
edges = [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]

print(count_components(n, edges) - 1)
