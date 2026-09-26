def de_bruijn_graph(patterns):
    graph = {}
    for pattern in patterns:
        prefix, suffix = pattern[:-1], pattern[1:]
        graph.setdefault(prefix, []).append(suffix)
    return graph

def eulerian_path(graph):
    out_degree = {}
    in_degree = {}
    nodes = set()
    for node, neighbors in graph.items():
        nodes.add(node)
        out_degree[node] = out_degree.get(node, 0) + len(neighbors)
        for neighbor in neighbors:
            nodes.add(neighbor)
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    start = next((n for n in nodes if out_degree.get(n, 0) - in_degree.get(n, 0) == 1), next(iter(nodes)))

    remaining = {node: list(neighbors) for node, neighbors in graph.items()}
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

def reconstruct_string(patterns):
    graph = de_bruijn_graph(patterns)
    path = eulerian_path(graph)
    genome = path[0]
    for node in path[1:]:
        genome += node[-1]
    return genome

patterns = ["CTTA", "ACCA", "TACC", "GGCT", "GCTT", "TTAC"]

print(reconstruct_string(patterns))
