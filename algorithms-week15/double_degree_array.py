def double_degree_array(n, edges):
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    return [sum(degree[nbr] for nbr in adj[v]) for v in range(1, n + 1)]

n = 5
edges = [(1, 2), (2, 3), (3, 4), (2, 4), (4, 5)]

print(" ".join(str(d) for d in double_degree_array(n, edges)))
