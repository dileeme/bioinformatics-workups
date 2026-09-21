def parse_graph(text):
    graph = {}
    for line in text.strip().splitlines():
        node, targets = line.split("->")
        graph.setdefault(node.strip(), []).extend(t.strip() for t in targets.split(","))
    return graph

def degrees(graph):
    out_degree = {node: len(targets) for node, targets in graph.items()}
    in_degree = {}
    for targets in graph.values():
        for t in targets:
            in_degree[t] = in_degree.get(t, 0) + 1
    for node in graph:
        in_degree.setdefault(node, 0)
    for node in list(in_degree):
        out_degree.setdefault(node, 0)
    return in_degree, out_degree

def maximal_non_branching_paths(graph):
    in_degree, out_degree = degrees(graph)
    remaining = {node: list(targets) for node, targets in graph.items()}
    visited_start = set()
    paths = []

    for node in list(remaining):
        if not (in_degree[node] == 1 and out_degree[node] == 1):
            while remaining.get(node):
                w = remaining[node].pop(0)
                path = [node, w]
                while in_degree.get(w) == 1 and out_degree.get(w) == 1:
                    w = remaining[w].pop(0)
                    path.append(w)
                paths.append(path)

    for node in remaining:
        if in_degree[node] == 1 and out_degree[node] == 1 and node not in visited_start:
            while remaining.get(node):
                cycle = [node]
                w = remaining[node].pop(0)
                cycle.append(w)
                visited_start.add(node)
                while w != node:
                    visited_start.add(w)
                    w = remaining[w].pop(0)
                    cycle.append(w)
                paths.append(cycle)

    return paths

text = """
1 -> 2
2 -> 3
3 -> 4
6 -> 7
7 -> 6
7 -> 8
8 -> 7
"""

graph = parse_graph(text)

for path in maximal_non_branching_paths(graph):
    print(" -> ".join(path))
