def build_paired_debruijn_graph(pairs, k):
    graph = {}
    for a, b in pairs:
        prefix = (a[:-1], b[:-1])
        suffix = (a[1:], b[1:])
        graph.setdefault(prefix, []).append((suffix, (a, b)))
        graph.setdefault(suffix, [])
    return graph

def find_eulerian_path(graph):
    out_degree = {node: len(edges) for node, edges in graph.items()}
    in_degree = {node: 0 for node in graph}
    for node, edges in graph.items():
        for target, _ in edges:
            in_degree[target] = in_degree.get(target, 0) + 1

    start = next(iter(graph))
    for node in graph:
        if out_degree.get(node, 0) - in_degree.get(node, 0) == 1:
            start = node
            break

    remaining = {node: list(edges) for node, edges in graph.items()}
    stack = [(start, None)]
    path = []
    while stack:
        node, pair = stack[-1]
        if remaining.get(node):
            next_node, next_pair = remaining[node].pop()
            stack.append((next_node, next_pair))
        else:
            path.append((node, pair))
            stack.pop()
    path.reverse()
    return path

def string_spelled_by_gapped_patterns(pairs, k, d):
    prefixes = [p for p, _ in pairs]
    suffixes = [s for _, s in pairs]

    prefix_string = prefixes[0]
    for prefix in prefixes[1:]:
        prefix_string += prefix[-1]

    suffix_string = suffixes[0]
    for suffix in suffixes[1:]:
        suffix_string += suffix[-1]

    overlap = len(prefix_string) - (k + d)
    if prefix_string[k + d:] != suffix_string[:overlap]:
        return None

    return prefix_string + suffix_string[overlap:]

def reconstruct_from_paired_composition(pairs, k, d):
    graph = build_paired_debruijn_graph(pairs, k)
    path = find_eulerian_path(graph)

    node_pairs = [pair for node, pair in path if pair is not None]
    return string_spelled_by_gapped_patterns(node_pairs, k, d)

k, d = 3, 1
pairs = [
    ("TAA", "GCC"),
    ("AAT", "CCA"),
    ("ATG", "CAT"),
    ("TGC", "ATG"),
    ("GCC", "TGG"),
    ("CCA", "GGG"),
    ("CAT", "GGA"),
    ("ATG", "GAT"),
    ("TGG", "ATG"),
    ("GGG", "TGT"),
    ("GGA", "GTT"),
]

print(reconstruct_from_paired_composition(pairs, k, d))
