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

adjacency = {
    0: [3],
    1: [0],
    2: [1, 6],
    3: [2],
    4: [2],
    5: [4],
    6: [5, 8],
    7: [9],
    8: [7],
    9: [6],
}

cycle = eulerian_cycle(adjacency, 0)
print("->".join(str(node) for node in cycle))
