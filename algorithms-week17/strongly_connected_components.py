def strongly_connected_components(n, edges):
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)

    visited = [False] * (n + 1)
    order = []

    def dfs1(start):
        stack = [(start, iter(adj[start]))]
        visited[start] = True
        while stack:
            node, it = stack[-1]
            advanced = False
            for neighbor in it:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, iter(adj[neighbor])))
                    advanced = True
                    break
            if not advanced:
                order.append(node)
                stack.pop()

    for v in range(1, n + 1):
        if not visited[v]:
            dfs1(v)

    assigned = [False] * (n + 1)
    components = 0

    def dfs2(start):
        stack = [start]
        assigned[start] = True
        while stack:
            node = stack.pop()
            for neighbor in radj[node]:
                if not assigned[neighbor]:
                    assigned[neighbor] = True
                    stack.append(neighbor)

    for v in reversed(order):
        if not assigned[v]:
            dfs2(v)
            components += 1

    return components

n = 8
edges = [
    (1, 2), (2, 5), (5, 1),
    (3, 4), (4, 3),
    (6, 7), (7, 6),
    (2, 3), (4, 6), (7, 8),
]

print(strongly_connected_components(n, edges))
