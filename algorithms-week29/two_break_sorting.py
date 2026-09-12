def chromosome_to_cycle(chromosome):
    nodes = []
    for block in chromosome:
        if block > 0:
            nodes += [2 * block - 1, 2 * block]
        else:
            nodes += [-2 * block, -2 * block - 1]
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

def genome_graph_to_genome(edges, blocks):
    colored_adj = {}
    for u, v in edges:
        colored_adj.setdefault(u, []).append(v)
        colored_adj.setdefault(v, []).append(u)

    visited = set()
    genome = []
    for start in range(1, 2 * blocks + 1):
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

def two_break_on_genome_graph(edges, i1, i2, i3, i4):
    edges = [e for e in edges if set(e) != {i1, i2} and set(e) != {i3, i4}]
    edges.append((i1, i3))
    edges.append((i2, i4))
    return edges

def count_blocks(genome):
    return sum(len(chromosome) for chromosome in genome)

def find_non_trivial_cycle(red_edges, blue_adjacency):
    red_adjacency = {}
    for u, v in red_edges:
        red_adjacency.setdefault(u, []).append(v)
        red_adjacency.setdefault(v, []).append(u)

    visited = set()
    for start in red_adjacency:
        if start in visited:
            continue
        current = start
        cycle = [start]
        visited.add(start)
        used_red = False
        while True:
            next_node = red_adjacency[current][0] if not used_red else blue_adjacency[current][0]
            used_red = not used_red
            if next_node == start:
                break
            cycle.append(next_node)
            visited.add(next_node)
            current = next_node
        if len(cycle) > 2:
            return cycle
    return None

def shortest_rearrangement_scenario(genome_p, genome_q):
    blocks = count_blocks(genome_p)
    red_edges = colored_edges(genome_p)
    blue_edges = colored_edges(genome_q)
    blue_adjacency = {}
    for u, v in blue_edges:
        blue_adjacency.setdefault(u, []).append(v)
        blue_adjacency.setdefault(v, []).append(u)

    genomes = [genome_p]
    while True:
        non_trivial = find_non_trivial_cycle(red_edges, blue_adjacency)
        if non_trivial is None:
            break
        n0, n1, n2, n3 = non_trivial[0], non_trivial[1], non_trivial[2], non_trivial[3]
        red_edges = two_break_on_genome_graph(red_edges, n1, n0, n2, n3)
        genome_p = genome_graph_to_genome(red_edges, blocks)
        genomes.append(genome_p)

    return genomes

def format_genome(genome):
    parts = []
    for chromosome in genome:
        parts.append("(" + " ".join(("+" if b > 0 else "") + str(b) for b in chromosome) + ")")
    return "".join(parts)

genome_p = [[1, 2, 3, 4, 5, 6]]
genome_q = [[1, -3, -6, -5], [2, -4]]

for genome in shortest_rearrangement_scenario(genome_p, genome_q):
    print(format_genome(genome))
