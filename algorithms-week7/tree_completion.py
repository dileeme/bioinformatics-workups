def min_edges_to_tree(n, edges):
    from collections import defaultdict, deque

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            bfs(node)
            components += 1

    return components - 1

n = 10
edges = [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]

print(min_edges_to_tree(n, edges))
