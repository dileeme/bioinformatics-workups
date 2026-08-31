import heapq

def dijkstra(n, adj, source):
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
    return dist

def shortest_cycle_through_edge(n, edges, x, y):
    adj = [[] for _ in range(n + 1)]
    edge_weight = None
    for u, v, w in edges:
        adj[u].append((v, w))
        if u == x and v == y:
            edge_weight = w

    dist = dijkstra(n, adj, y)
    if dist[x] == -1:
        return -1
    return edge_weight + dist[x]

n = 4
edges = [(1, 2, 2), (2, 3, 3), (3, 1, 4), (1, 4, 10)]

print(shortest_cycle_through_edge(n, edges, 1, 2))
