def chromosome_to_cycle(chromosome):
    nodes = []
    for block in chromosome:
        if block > 0:
            nodes.append(2 * block - 1)
            nodes.append(2 * block)
        else:
            nodes.append(-2 * block)
            nodes.append(-2 * block - 1)
    return nodes

def colored_edges(genome):
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        n = len(nodes)
        for i in range(0, n, 2):
            edges.append((nodes[i + 1], nodes[(i + 2) % n]))
    return edges

genome = [[1, -2, -3]]

print(", ".join(f"({u}, {v})" for u, v in colored_edges(genome)))
