from itertools import product

def build_debruijn_graph(kmers):
    adj = {}
    for kmer in kmers:
        prefix, suffix = kmer[:-1], kmer[1:]
        adj.setdefault(prefix, []).append(suffix)
    return adj

def eulerian_cycle(adj, start):
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
    return circuit

def k_universal_circular_string(k):
    kmers = ["".join(bits) for bits in product("01", repeat=k)]
    adj = build_debruijn_graph(kmers)
    start = kmers[0][:-1]
    cycle = eulerian_cycle(adj, start)
    return "".join(node[0] for node in cycle[:-1])

k = 4

print(k_universal_circular_string(k))
