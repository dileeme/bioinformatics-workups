def find_start_node(adj):
    out_degree = {node: len(neighbors) for node, neighbors in adj.items()}
    in_degree = {}
    for neighbors in adj.values():
        for node in neighbors:
            in_degree[node] = in_degree.get(node, 0) + 1

    for node in out_degree:
        if out_degree[node] - in_degree.get(node, 0) == 1:
            return node
    return next(iter(adj))

def eulerian_path(adj):
    remaining = {node: list(neighbors) for node, neighbors in adj.items()}
    start = find_start_node(adj)
    stack = [start]
    path = []
    while stack:
        node = stack[-1]
        if remaining.get(node):
            stack.append(remaining[node].pop())
        else:
            path.append(stack.pop())
    path.reverse()
    return path

adjacency = {
    0: [2],
    1: [3],
    2: [1],
    3: [0, 4],
    6: [3, 7],
    7: [8],
    8: [9],
    9: [6],
}

path = eulerian_path(adjacency)
print("->".join(str(node) for node in path))
