def pair(node):
    return node + 1 if node % 2 == 1 else node - 1

def cycle_to_chromosome(nodes):
    chromosome = []
    for j in range(len(nodes) // 2):
        a, b = nodes[2 * j], nodes[2 * j + 1]
        if a < b:
            chromosome.append(b // 2)
        else:
            chromosome.append(-(a // 2))
    return chromosome

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

def format_genome(genome):
    parts = []
    for chromosome in genome:
        parts.append("(" + " ".join(f"+{b}" if b > 0 else str(b) for b in chromosome) + ")")
    return "".join(parts)

edges = [(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)]

print(format_genome(graph_to_genome(edges)))
