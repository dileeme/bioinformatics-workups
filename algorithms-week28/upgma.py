def upgma(matrix, n):
    clusters = {i: [i] for i in range(n)}
    age = {i: 0.0 for i in range(n)}
    tree = {i: {} for i in range(n)}
    dist = {i: {j: matrix[i][j] for j in range(n) if j != i} for i in range(n)}
    next_node = n

    active = list(range(n))
    while len(active) > 1:
        best_pair = None
        best_dist = None
        for a_idx in range(len(active)):
            for b_idx in range(a_idx + 1, len(active)):
                a, b = active[a_idx], active[b_idx]
                if best_dist is None or dist[a][b] < best_dist:
                    best_dist = dist[a][b]
                    best_pair = (a, b)

        a, b = best_pair
        new_node = next_node
        next_node += 1

        merged = clusters[a] + clusters[b]
        clusters[new_node] = merged
        age[new_node] = best_dist / 2.0

        tree[new_node] = {}
        tree[a][new_node] = age[new_node] - age[a]
        tree[new_node][a] = age[new_node] - age[a]
        tree[b][new_node] = age[new_node] - age[b]
        tree[new_node][b] = age[new_node] - age[b]

        dist[new_node] = {}
        for c in active:
            if c == a or c == b:
                continue
            new_dist = (dist[a][c] * len(clusters[a]) + dist[b][c] * len(clusters[b])) / len(merged)
            dist[new_node][c] = new_dist
            dist[c][new_node] = new_dist

        active = [c for c in active if c != a and c != b]
        active.append(new_node)

    return tree

n = 4
matrix = [
    [0, 20, 17, 11],
    [20, 0, 20, 13],
    [17, 20, 0, 10],
    [11, 13, 10, 0],
]

tree = upgma(matrix, n)

edges = []
for u in tree:
    for v, w in tree[u].items():
        edges.append(f"{u}->{v}:{w:.3f}")
for edge in sorted(edges):
    print(edge)
