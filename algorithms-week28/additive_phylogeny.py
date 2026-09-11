def limb_length(n, j, matrix):
    best = None
    for i in range(n):
        if i == j:
            continue
        for k in range(n):
            if k == j or k == i:
                continue
            value = (matrix[i][j] + matrix[j][k] - matrix[i][k]) // 2
            if best is None or value < best:
                best = value
    return best

def additive_phylogeny(matrix, labels, tree, next_node):
    n = len(matrix)
    if n == 2:
        tree.setdefault(labels[0], {})[labels[1]] = matrix[0][1]
        tree.setdefault(labels[1], {})[labels[0]] = matrix[0][1]
        return tree, next_node

    limb = limb_length(n, n - 1, matrix)
    for j in range(n - 1):
        matrix[j][n - 1] -= limb
        matrix[n - 1][j] = matrix[j][n - 1]

    i, k = 0, 1
    for a in range(n - 1):
        for b in range(n - 1):
            if a != b and matrix[a][n - 1] + matrix[b][n - 1] == matrix[a][b]:
                i, k = a, b
                break

    x = matrix[i][n - 1]
    leaf_label = labels[n - 1]
    inner_matrix = [row[:n - 1] for row in matrix[:n - 1]]
    inner_labels = labels[:n - 1]

    tree, next_node = additive_phylogeny(inner_matrix, inner_labels, tree, next_node)

    path = find_path(tree, inner_labels[i], inner_labels[k])
    attach_point, remaining = walk_path(tree, path, x)

    if remaining == 0:
        tree.setdefault(attach_point, {})[leaf_label] = limb
        tree.setdefault(leaf_label, {})[attach_point] = limb
    else:
        u, v, dist_from_u = attach_point
        new_node = next_node
        next_node += 1
        weight_uv = tree[u][v]
        tree[u].pop(v)
        tree[v].pop(u)
        tree.setdefault(u, {})[new_node] = dist_from_u
        tree.setdefault(new_node, {})[u] = dist_from_u
        tree.setdefault(v, {})[new_node] = weight_uv - dist_from_u
        tree.setdefault(new_node, {})[v] = weight_uv - dist_from_u
        tree.setdefault(new_node, {})[leaf_label] = limb
        tree.setdefault(leaf_label, {})[new_node] = limb

    return tree, next_node

def find_path(tree, start, end):
    stack = [(start, [start])]
    visited = {start}
    while stack:
        node, path = stack.pop()
        if node == end:
            return path
        for neighbor in tree[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    return None

def walk_path(tree, path, x):
    remaining = x
    for a, b in zip(path, path[1:]):
        weight = tree[a][b]
        if remaining < weight:
            return (a, b, remaining), remaining
        if remaining == weight:
            return b, 0
        remaining -= weight
    return path[-1], 0

n = 4
matrix = [
    [0, 13, 21, 22],
    [13, 0, 12, 13],
    [21, 12, 0, 13],
    [22, 13, 13, 0],
]
labels = list(range(n))

tree, _ = additive_phylogeny([row[:] for row in matrix], labels, {}, n)

edges = []
for u in tree:
    for v, w in tree[u].items():
        edges.append(f"{u}->{v}:{w}")
for edge in sorted(edges):
    print(edge)
