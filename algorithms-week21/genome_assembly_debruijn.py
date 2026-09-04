def reverse_complement(dna):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(dna))

def build_debruijn_graph(reads, k):
    adj = {}
    for read in reads:
        for seq in (read, reverse_complement(read)):
            for i in range(len(seq) - k + 1):
                prefix = seq[i:i + k - 1]
                suffix = seq[i + 1:i + k]
                adj.setdefault(prefix, []).append(suffix)
    return adj

def eulerian_circuit(adj, start):
    remaining = {node: list(neighbors) for node, neighbors in adj.items()}
    stack = [start]
    circuit = []
    while stack:
        node = stack[-1]
        if remaining.get(node):
            stack.append(remaining[node].pop())
        else:
            circuit.append(stack.pop())
    circuit.reverse()
    fully_used = all(not remaining.get(node) for node in circuit)
    return circuit, fully_used

def assemble_genome(reads, k):
    adj = build_debruijn_graph(reads, k)
    start = next(iter(adj))
    circuit, fully_used = eulerian_circuit(adj, start)
    if not fully_used or circuit[0] != circuit[-1]:
        return None
    genome = circuit[0]
    for node in circuit[1:]:
        genome += node[-1]
    return genome[:-(k - 1)]

reads = ["GATT", "ATTA", "TTAC", "TACA", "ACAG", "CAGA", "AGAT"]
k = 4

print(assemble_genome(reads, k))
