def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, x, y):
    x, y = find(parent, x), find(parent, y)
    if x == y:
        return False
    if rank[x] < rank[y]:
        x, y = y, x
    parent[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1
    return True

def minimum_spanning_tree_weight(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total = 0
    components = n
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(parent, rank, u, v):
            total += w
            components -= 1
    return total if components == 1 else -1

n = 5
edges = [
    (1, 2, 5),
    (1, 3, 3),
    (2, 3, 1),
    (2, 4, 4),
    (3, 4, 2),
    (4, 5, 6),
]

print(minimum_spanning_tree_weight(n, edges))
