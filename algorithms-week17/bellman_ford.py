def bellman_ford(n, edges, source=1):
    dist = [None] * (n + 1)
    dist[source] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] is not None and (dist[v] is None or dist[u] + w < dist[v]):
                dist[v] = dist[u] + w

    return [d if d is not None else -1 for d in dist[1:]]

n = 6
edges = [
    (1, 2, 6), (1, 3, 7), (2, 3, 8), (2, 4, 5), (2, 5, -4),
    (3, 4, -3), (3, 5, 9), (4, 2, -2), (5, 1, 2), (5, 4, 7),
]

print(" ".join(str(d) for d in bellman_ford(n, edges)))
