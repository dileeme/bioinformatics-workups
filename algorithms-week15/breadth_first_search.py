from collections import deque

def bfs_distances(n, edges, source=1):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    dist = [-1] * (n + 1)
    dist[source] = 0
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist[1:]

n = 7
edges = [(1, 2), (2, 3), (3, 4), (1, 5), (5, 6)]

print(" ".join(str(d) for d in bfs_distances(n, edges)))
