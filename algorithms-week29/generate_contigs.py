def debruijn_graph_from_kmers(kmers):
    graph = {}
    for kmer in kmers:
        prefix, suffix = kmer[:-1], kmer[1:]
        graph.setdefault(prefix, [])
        graph.setdefault(suffix, [])
        graph[prefix].append(suffix)
    return graph

def maximal_non_branching_paths(graph):
    in_degree = {node: 0 for node in graph}
    out_degree = {node: len(graph[node]) for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    remaining = {node: list(neighbors) for node, neighbors in graph.items()}
    paths = []

    for node in graph:
        if not (in_degree.get(node, 0) == 1 and out_degree.get(node, 0) == 1):
            for neighbor in list(remaining[node]):
                remaining[node].remove(neighbor)
                path = [node, neighbor]
                while in_degree.get(path[-1], 0) == 1 and out_degree.get(path[-1], 0) == 1:
                    next_node = remaining[path[-1]].pop(0)
                    path.append(next_node)
                paths.append(path)

    visited = {node: False for node in graph}
    for path in paths:
        for node in path:
            visited[node] = True

    for node in graph:
        if not visited[node] and in_degree.get(node, 0) == 1 and out_degree.get(node, 0) == 1:
            cycle = [node]
            current = remaining[node].pop(0)
            while current != node:
                visited[current] = True
                cycle.append(current)
                current = remaining[current].pop(0)
            cycle.append(node)
            paths.append(cycle)

    return paths

def path_to_string(path):
    result = path[0]
    for node in path[1:]:
        result += node[-1]
    return result

def generate_contigs(kmers):
    graph = debruijn_graph_from_kmers(kmers)
    paths = maximal_non_branching_paths(graph)
    return [path_to_string(path) for path in paths]

kmers = ["ATG", "ATG", "TGT", "TGG", "CAT", "GGA", "GAT", "AGA"]

for contig in sorted(generate_contigs(kmers)):
    print(contig)
