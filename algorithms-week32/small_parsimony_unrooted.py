def hamming_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

def small_parsimony_unrooted(edges, leaf_labels):
    adjacency = {}
    for a, b in edges:
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)

    v, w = next((a, b) for a, b in edges if a not in leaf_labels and b not in leaf_labels)
    adjacency[v].discard(w)
    adjacency[w].discard(v)

    root = "root"
    children = {root: [v, w]}

    def build(node, parent):
        for neighbor in adjacency.get(node, ()):
            if neighbor != parent:
                children.setdefault(node, []).append(neighbor)
                build(neighbor, node)

    build(v, root)
    build(w, root)

    all_nodes = set(children) | {n for kids in children.values() for n in kids} | set(leaf_labels)
    alphabet = "ACGT"
    length = len(next(iter(leaf_labels.values())))
    labels = {n: [""] * length for n in all_nodes if n not in leaf_labels}
    total_score = 0

    for pos in range(length):
        cost = {}

        def compute(node):
            if node in leaf_labels:
                actual = leaf_labels[node][pos]
                cost[node] = {a: (0 if a == actual else float("inf")) for a in alphabet}
                return
            for child in children[node]:
                compute(child)
            cost[node] = {}
            for a in alphabet:
                total = 0
                for child in children[node]:
                    total += min(cost[child][b] + (0 if a == b else 1) for b in alphabet)
                cost[node][a] = total

        compute(root)
        total_score += min(cost[root].values())

        def assign(node, parent_symbol):
            if node in leaf_labels:
                return
            if parent_symbol is None:
                symbol = min(alphabet, key=lambda a: cost[node][a])
            else:
                symbol = min(alphabet, key=lambda a: cost[node][a] + (0 if a == parent_symbol else 1))
            labels[node][pos] = symbol
            for child in children[node]:
                assign(child, symbol)

        assign(root, None)

    labels = {n: "".join(chars) for n, chars in labels.items()}
    labels.update(leaf_labels)

    output_edges = []
    for a, b in edges:
        dist = hamming_distance(labels[a], labels[b])
        output_edges.append((a, b, dist))
        output_edges.append((b, a, dist))

    return total_score, labels, output_edges

leaf_labels = {
    "TCGGCCAA": "TCGGCCAA",
    "CCTGGCTG": "CCTGGCTG",
    "CACAGGAT": "CACAGGAT",
    "TGAGTACC": "TGAGTACC",
}
edges = [
    ("TCGGCCAA", "4"),
    ("CCTGGCTG", "4"),
    ("CACAGGAT", "5"),
    ("TGAGTACC", "5"),
    ("4", "5"),
]

score, labels, output_edges = small_parsimony_unrooted(edges, leaf_labels)

print(score)
for a, b, dist in output_edges:
    print(f"{labels[a]}->{labels[b]}:{dist}")
