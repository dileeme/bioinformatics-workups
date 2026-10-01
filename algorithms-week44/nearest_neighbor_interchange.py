def parse_tree(lines):
    adjacency = {}
    for line in lines:
        a, b = line.split("->")
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)
    return adjacency

def format_tree(adjacency):
    edges = []
    for node in sorted(adjacency):
        for neighbor in sorted(adjacency[node]):
            edges.append(f"{node}->{neighbor}")
    return edges

def nearest_neighbors(adjacency, a, b):
    a_neighbors = sorted(adjacency[a] - {b})
    b_neighbors = sorted(adjacency[b] - {a})
    a1, a2 = a_neighbors
    b1, b2 = b_neighbors

    trees = []
    for swapped in ((b1, a1), (b2, a1)):
        new_b_partner, new_a_partner = swapped
        new_adjacency = {node: set(neighbors) for node, neighbors in adjacency.items()}
        new_adjacency[a].discard(new_a_partner)
        new_adjacency[a].add(new_b_partner)
        new_adjacency[new_b_partner].discard(b)
        new_adjacency[new_b_partner].add(a)
        new_adjacency[b].discard(new_b_partner)
        new_adjacency[b].add(new_a_partner)
        new_adjacency[new_a_partner].discard(a)
        new_adjacency[new_a_partner].add(b)
        trees.append(new_adjacency)
    return trees

edge = ("4", "5")
tree_lines = [
    "0->4",
    "4->0",
    "1->4",
    "4->1",
    "2->5",
    "5->2",
    "3->5",
    "5->3",
    "4->5",
    "5->4",
]

adjacency = parse_tree(tree_lines)
for tree in nearest_neighbors(adjacency, *edge):
    for edge_str in format_tree(tree):
        print(edge_str)
    print()
