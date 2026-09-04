def hamiltonian_path(n, edges):
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    path = []
    available = [v for v in range(1, n + 1) if indegree[v] == 0]
    for _ in range(n):
        if len(available) != 1:
            return None
        node = available.pop()
        path.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                available.append(neighbor)

    for i in range(len(path) - 1):
        if path[i + 1] not in adj[path[i]]:
            return None
    return path

graphs = [
    (4, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]),
    (4, [(1, 2), (3, 4)]),
]

for n, edges in graphs:
    result = hamiltonian_path(n, edges)
    if result is None:
        print(-1)
    else:
        print(1)
        print(" ".join(str(v) for v in result))
