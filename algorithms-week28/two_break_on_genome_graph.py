def two_break_on_genome_graph(edges, i1, i2, i3, i4):
    edges = [e for e in edges if set(e) != {i1, i2} and set(e) != {i3, i4}]
    edges.append((i1, i3))
    edges.append((i2, i4))
    return edges

edges = [(2, 4), (3, 8), (7, 5), (6, 1)]
i1, i2, i3, i4 = 1, 6, 3, 8

result = two_break_on_genome_graph(edges, i1, i2, i3, i4)
print(", ".join(f"({u}, {v})" for u, v in result))
