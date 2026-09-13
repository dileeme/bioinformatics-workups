import itertools

def neighbor_joining(distance, labels):
    distance = {i: dict(row) for i, row in distance.items()}
    active = set(labels)
    next_id = max(labels) + 1
    edges = {}

    def add_edge(u, v, w):
        edges.setdefault(u, {})[v] = w
        edges.setdefault(v, {})[u] = w

    while len(active) > 2:
        n = len(active)
        total = {i: sum(distance[i][j] for j in active if j != i) for i in active}

        best = None
        for i, j in itertools.combinations(active, 2):
            score = (n - 2) * distance[i][j] - total[i] - total[j]
            if best is None or score < best[0]:
                best = (score, i, j)
        _, i, j = best

        m = next_id
        next_id += 1
        delta_i = distance[i][j] / 2 + (total[i] - total[j]) / (2 * (n - 2))
        delta_j = distance[i][j] - delta_i
        add_edge(i, m, delta_i)
        add_edge(j, m, delta_j)

        distance[m] = {}
        for k in active:
            if k != i and k != j:
                dk = (distance[k][i] + distance[k][j] - distance[i][j]) / 2
                distance[m][k] = dk
                distance[k][m] = dk

        active.discard(i)
        active.discard(j)
        active.add(m)

    i, j = tuple(active)
    add_edge(i, j, distance[i][j])
    return edges

n = 5
labels = list(range(n))
matrix = [
    [0, 5, 13, 10, 13],
    [5, 0, 14, 11, 14],
    [13, 14, 0, 5, 12],
    [10, 11, 5, 0, 9],
    [13, 14, 12, 9, 0],
]
distance = {i: {j: matrix[i][j] for j in labels} for i in labels}

edges = neighbor_joining(distance, labels)
for u in sorted(edges):
    for v, w in sorted(edges[u].items()):
        print(f"{u}->{v}:{w:.3f}")
