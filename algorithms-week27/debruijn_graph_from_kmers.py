def debruijn_graph_from_kmers(kmers):
    graph = {}
    for kmer in kmers:
        prefix, suffix = kmer[:-1], kmer[1:]
        graph.setdefault(prefix, []).append(suffix)
    return graph

kmers = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]

graph = debruijn_graph_from_kmers(kmers)
for node in sorted(graph):
    print(f"{node} -> {','.join(sorted(graph[node]))}")
