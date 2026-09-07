def debruijn_graph(text, k):
    graph = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prefix, suffix = kmer[:-1], kmer[1:]
        graph.setdefault(prefix, []).append(suffix)
    return graph

text = "AAGATTCTCTAC"
k = 4

graph = debruijn_graph(text, k)
for node in sorted(graph):
    print(f"{node} -> {','.join(graph[node])}")
