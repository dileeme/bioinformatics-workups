import heapq

def dijkstra(n, edges, source=1):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [-1] * (n + 1)
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            new_dist = d + weight
            if dist[neighbor] == -1 or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist[1:]

n = 7
edges = [
    (1, 2, 4), (1, 3, 1), (3, 2, 1), (2, 4, 1),
    (3, 4, 5), (4, 5, 3), (5, 6, 2), (2, 6, 10),
]

print(" ".join(str(d) for d in dijkstra(n, edges)))
