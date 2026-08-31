def has_negative_cycle(n, edges):
    dist = [0] * (n + 1)
    parent = None
    for i in range(n):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
                if i == n - 1:
                    return True
        if not updated:
            return False
    return False

graphs = [
    (3, [(1, 2, 1), (2, 3, -1), (3, 1, -1)]),
    (3, [(1, 2, 1), (2, 3, 1), (3, 1, 1)]),
]

print(" ".join("1" if has_negative_cycle(n, edges) else "-1" for n, edges in graphs))
