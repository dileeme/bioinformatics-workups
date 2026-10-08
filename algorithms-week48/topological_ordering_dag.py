def topological_ordering(edges):
    adjacency = {}
    nodes = set()
    for u, v in edges:
        adjacency.setdefault(u, []).append(v)
        nodes.add(u)
        nodes.add(v)

    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        for neighbor in adjacency.get(node, []):
            if neighbor not in visited:
                visit(neighbor)
        order.append(node)

    for node in sorted(nodes):
        if node not in visited:
            visit(node)

    return order[::-1]

edges = [(1, 2), (2, 3), (4, 2), (5, 4), (1, 5), (1, 4), (5, 3), (1, 3)]

print(", ".join(str(node) for node in topological_ordering(edges)))
