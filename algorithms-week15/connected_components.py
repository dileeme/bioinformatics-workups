def count_connected_components(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)

    def dfs(start):
        stack = [start]
        visited[start] = True
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    components = 0
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)
            components += 1

    return components

n = 8
edges = [(1, 2), (2, 3), (4, 5), (6, 7), (7, 8)]

print(count_connected_components(n, edges))
