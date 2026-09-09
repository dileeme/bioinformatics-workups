def chromosome_to_cycle(chromosome):
    nodes = []
    for block in chromosome:
        if block > 0:
            nodes += [2 * block - 1, 2 * block]
        else:
            nodes += [-2 * block, -2 * block - 1]
    return nodes

def colored_edges(genome):
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        n = len(nodes)
        for i in range(0, n, 2):
            edges.append((nodes[i + 1], nodes[(i + 2) % n]))
    return edges

def count_blocks(genome):
    return sum(len(chromosome) for chromosome in genome)

def two_break_distance(genome_p, genome_q):
    blocks = count_blocks(genome_p)
    parent = list(range(2 * blocks + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for u, v in colored_edges(genome_p) + colored_edges(genome_q):
        union(u, v)

    cycles = len({find(node) for node in range(1, 2 * blocks + 1)})
    return blocks - cycles

genome_p = [[1, 2, 3, 4, 5, 6]]
genome_q = [[1, -3, -6, -5], [2, -4]]

print(two_break_distance(genome_p, genome_q))
