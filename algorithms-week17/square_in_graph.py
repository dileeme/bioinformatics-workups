def has_square(n, edges):
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    for u in range(1, n + 1):
        for w in range(u + 1, n + 1):
            if len(adj[u] & adj[w]) >= 2:
                return True
    return False

graphs = [
    (4, [(1, 2), (2, 3), (3, 4), (4, 1)]),
    (3, [(1, 2), (2, 3), (3, 1)]),
]

print(" ".join("1" if has_square(n, edges) else "-1" for n, edges in graphs))
