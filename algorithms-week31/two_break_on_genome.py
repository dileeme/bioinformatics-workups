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

def cycle_to_chromosome(nodes):
    chromosome = []
    for j in range(len(nodes) // 2):
        a, b = nodes[2 * j], nodes[2 * j + 1]
        if a < b:
            chromosome.append(b // 2)
        else:
            chromosome.append(-(a // 2))
    return chromosome

def colored_edges(genome):
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        n = len(nodes)
        for i in range(0, n, 2):
            edges.append((nodes[i + 1], nodes[(i + 2) % n]))
    return edges

def pair(node):
    return node + 1 if node % 2 == 1 else node - 1

def graph_to_genome(edges):
    colored_adj = {}
    for u, v in edges:
        colored_adj.setdefault(u, []).append(v)
        colored_adj.setdefault(v, []).append(u)

    nodes = {n for edge in edges for n in edge}
    visited = set()
    genome = []

    for start in sorted(nodes):
        if start in visited:
            continue
        cycle = [start]
        visited.add(start)
        current = pair(start)
        cycle.append(current)
        visited.add(current)
        while True:
            next_node = colored_adj[current][0]
            if next_node == start:
                break
            cycle.append(next_node)
            visited.add(next_node)
            current = pair(next_node)
            cycle.append(current)
            visited.add(current)
        genome.append(cycle_to_chromosome(cycle))

    return genome

def two_break_on_genome(genome, i1, i2, i3, i4):
    edges = colored_edges(genome)
    edges = [e for e in edges if set(e) != {i1, i2} and set(e) != {i3, i4}]
    edges.append((i1, i3))
    edges.append((i2, i4))
    return graph_to_genome(edges)

def format_genome(genome):
    parts = []
    for chromosome in genome:
        parts.append("(" + " ".join(f"+{b}" if b > 0 else str(b) for b in chromosome) + ")")
    return "".join(parts)

genome = [[1, -2, -4, 3]]
i1, i2, i3, i4 = 1, 6, 3, 8

print(format_genome(two_break_on_genome(genome, i1, i2, i3, i4)))
