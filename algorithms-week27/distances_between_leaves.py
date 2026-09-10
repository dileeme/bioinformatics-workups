from collections import deque

def build_adjacency(n, edges):
    adjacency = {}
    for u, v, weight in edges:
        adjacency.setdefault(u, []).append((v, weight))
        adjacency.setdefault(v, []).append((u, weight))
    return adjacency

def distances_from_leaf(adjacency, source, n):
    distances = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor, weight in adjacency[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + weight
                queue.append(neighbor)
    return [distances[leaf] for leaf in range(n)]

def distance_matrix(n, edges):
    adjacency = build_adjacency(n, edges)
    return [distances_from_leaf(adjacency, leaf, n) for leaf in range(n)]

n = 4
edges = [
    (0, 4, 11),
    (1, 4, 2),
    (2, 5, 6),
    (3, 5, 7),
    (4, 0, 11),
    (4, 1, 2),
    (4, 5, 4),
    (5, 4, 4),
    (5, 3, 7),
    (5, 2, 6),
]

for row in distance_matrix(n, edges):
    print(" ".join(str(d) for d in row))
