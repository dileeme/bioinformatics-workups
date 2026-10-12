def build_edges(reads):
    edges = []
    for read in reads:
        edges.append((read[:-1], read[1:]))
    return edges

def find_all_circuits(edges, start):
    n = len(edges)
    used = [False] * n
    outgoing = {}
    for idx, (u, v) in enumerate(edges):
        outgoing.setdefault(u, []).append(idx)

    results = []
    path = [start]

    def backtrack(node, remaining):
        if remaining == 0:
            if node == start:
                results.append(list(path))
            return
        for idx in outgoing.get(node, []):
            if not used[idx]:
                used[idx] = True
                path.append(edges[idx][1])
                backtrack(edges[idx][1], remaining - 1)
                path.pop()
                used[idx] = False

    backtrack(start, n)
    return results

def circuit_to_genome(circuit, num_edges):
    linear = circuit[0] + "".join(node[-1] for node in circuit[1:])
    return linear[:num_edges]

def smallest_rotation(s):
    return min(s[i:] + s[:i] for i in range(len(s)))

def assemble_with_repeats(reads):
    edges = build_edges(reads)
    start = edges[0][0]
    genomes = set()
    for circuit in find_all_circuits(edges, start):
        genome = circuit_to_genome(circuit, len(reads))
        genomes.add(smallest_rotation(genome))
    return sorted(genomes)

reads = ["ACG", "CGT", "GTA", "TAC", "ACG", "CGA", "GAA", "AAC"]

for genome in assemble_with_repeats(reads):
    print(genome)
