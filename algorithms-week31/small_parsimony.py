def small_parsimony(edges, leaf_labels):
    children = {}
    all_nodes = set()
    for p, c in edges:
        children.setdefault(p, []).append(c)
        all_nodes.add(p)
        all_nodes.add(c)
    child_nodes = {c for _, c in edges}
    root = next(n for n in all_nodes if n not in child_nodes)

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

    return total_score, {n: "".join(chars) for n, chars in labels.items()}

leaf_labels = {
    "GCAGGGTA": "GCAGGGTA",
    "TTTATCCC": "TTTATCCC",
    "CAAATCCC": "CAAATCCC",
    "ATTGCCTC": "ATTGCCTC",
}
edges = [
    (4, "GCAGGGTA"), (4, "TTTATCCC"),
    (5, "CAAATCCC"), (5, "ATTGCCTC"),
    (6, 4), (6, 5),
]

score, internal_labels = small_parsimony(edges, leaf_labels)

print(score)
for node in sorted(internal_labels):
    print(f"{node}->{internal_labels[node]}")
