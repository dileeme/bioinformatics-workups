def topological_sort(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * (n + 1)
    order = []

    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        order.append(node)

    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)

    return order[::-1]

n = 4
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]

print(" ".join(str(v) for v in topological_sort(n, edges)))
