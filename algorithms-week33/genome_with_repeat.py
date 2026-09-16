from collections import defaultdict

def build_de_bruijn(reads):
    out_edges = defaultdict(list)
    for read in reads:
        out_edges[read[:-1]].append((read[1:], read))
    return out_edges

def reconstruct_genomes(reads):
    out_edges = build_de_bruijn(reads)
    repeat_node = next(node for node, edges in out_edges.items() if len(edges) == 2)
    used = {node: 0 for node in out_edges}

    def walk_cycle(target, kmer):
        path = [kmer]
        node = target
        while node != repeat_node:
            index = used[node]
            target, kmer = out_edges[node][index]
            used[node] += 1
            path.append(kmer)
            node = target
        return path

    (target1, kmer1), (target2, kmer2) = out_edges[repeat_node]
    cycle1 = walk_cycle(target1, kmer1)
    cycle2 = walk_cycle(target2, kmer2)

    genome_a = "".join(kmer[0] for kmer in cycle1 + cycle2)
    genome_b = "".join(kmer[0] for kmer in cycle2 + cycle1)
    return genome_a, genome_b

reads = [
    'CTAAAC', 'TGTATT', 'GAACGT', 'GTTGTA', 'GTTGCC', 'CCTAAA', 'TTGAAC',
    'ACCCGT', 'AACCCG', 'CGTTGT', 'ACGTTG', 'CCGTTG', 'TGCCTA', 'AAACCC',
    'TGAACG', 'TTTGAA', 'CGTTGC', 'TTGCCT', 'AACGTT', 'TTGTAT', 'ATTTGA',
    'CCCGTT', 'GCCTAA', 'GTATTT', 'TATTTG', 'TAAACC',
]

for genome in reconstruct_genomes(reads):
    print(genome)
