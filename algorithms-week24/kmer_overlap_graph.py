def build_overlap_graph(kmers):
    graph = {}
    for i, a in enumerate(kmers):
        for j, b in enumerate(kmers):
            if i != j and a[1:] == b[:-1]:
                graph.setdefault(a, []).append(b)
    return graph

kmers = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]

graph = build_overlap_graph(kmers)
for node in sorted(graph):
    for neighbor in graph[node]:
        print(f"{node} -> {neighbor}")
