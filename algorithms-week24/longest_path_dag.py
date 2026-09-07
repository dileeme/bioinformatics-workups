from collections import deque

def longest_path(n, edges, source, sink):
    graph = {i: [] for i in range(n + 1)}
    indegree = {i: 0 for i in range(n + 1)}
    for a, b, w in edges:
        graph[a].append((b, w))
        indegree[b] += 1

    queue = deque(i for i in range(n + 1) if indegree[i] == 0)
    order = []
    remaining = dict(indegree)
    while queue:
        node = queue.popleft()
        order.append(node)
        for b, w in graph[node]:
            remaining[b] -= 1
            if remaining[b] == 0:
                queue.append(b)

    dist = {i: float("-inf") for i in range(n + 1)}
    dist[source] = 0
    backtrack = {}
    for node in order:
        if dist[node] == float("-inf"):
            continue
        for b, w in graph[node]:
            if dist[node] + w > dist[b]:
                dist[b] = dist[node] + w
                backtrack[b] = node

    path = [sink]
    while path[-1] != source:
        path.append(backtrack[path[-1]])
    path.reverse()
    return dist[sink], path

n = 4
source = 0
sink = 4
edges = [(0, 1, 7), (0, 2, 4), (2, 3, 2), (1, 4, 1), (3, 4, 3)]

length, path = longest_path(n, edges, source, sink)
print(length)
print(" ".join(str(p) for p in path))
