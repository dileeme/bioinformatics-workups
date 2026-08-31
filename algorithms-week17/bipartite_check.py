def is_bipartite(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    color = [None] * (n + 1)
    for start in range(1, n + 1):
        if color[start] is not None:
            continue
        color[start] = 0
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if color[neighbor] is None:
                    color[neighbor] = 1 - color[node]
                    stack.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True

graphs = [
    (4, [(1, 2), (2, 3), (3, 4), (4, 1)]),
    (3, [(1, 2), (2, 3), (3, 1)]),
]

print(" ".join("1" if is_bipartite(n, edges) else "-1" for n, edges in graphs))
