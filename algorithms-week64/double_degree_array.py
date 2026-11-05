def double_degree_array(n, edges):
    degree = [0] * (n + 1)
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    double_degree = [0] * (n + 1)
    for a, b in edges:
        double_degree[a] += degree[b]
        double_degree[b] += degree[a]
    return double_degree[1:]

n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (2, 4)]

print(" ".join(str(d) for d in double_degree_array(n, edges)))
