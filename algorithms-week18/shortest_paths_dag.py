from collections import deque

def topological_order(n, adj):
    indeg = [0] * (n + 1)
    for u in range(1, n + 1):
        for v, _ in adj[u]:
            indeg[v] += 1
    queue = deque(u for u in range(1, n + 1) if indeg[u] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, _ in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    return order

def shortest_paths_dag(n, edges, source=1):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [None] * (n + 1)
    dist[source] = 0
    for u in topological_order(n, adj):
        if dist[u] is None:
            continue
        for v, w in adj[u]:
            if dist[v] is None or dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist[1:]

n = 7
edges = [
    (1, 2, 5), (1, 3, 3), (2, 3, 2), (2, 4, 6),
    (3, 4, 7), (3, 5, 4), (4, 5, -1), (4, 6, 1), (5, 6, -2),
]

distances = shortest_paths_dag(n, edges)
print(" ".join("x" if d is None else str(d) for d in distances))
