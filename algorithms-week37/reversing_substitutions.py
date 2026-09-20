def find_root(edges):
    children = {c for _, c in edges}
    parents = {p for p, _ in edges}
    return next(n for n in parents if n not in children)

def reversing_substitutions(edges, labels):
    parent_of = {c: p for p, c in edges}
    root = find_root(edges)
    length = len(next(iter(labels.values())))
    results = []

    for node in labels:
        if node == root:
            continue
        parent = parent_of[node]
        for pos in range(length):
            x = labels[node][pos]
            y = labels[parent][pos]
            if x == y:
                continue
            ancestor = parent
            while ancestor in parent_of and labels[parent_of[ancestor]][pos] == y:
                ancestor = parent_of[ancestor]
            if ancestor not in parent_of:
                continue
            boundary = parent_of[ancestor]
            if labels[boundary][pos] == x:
                results.append((boundary, node, pos + 1, x + y + x))

    return results

edges = [
    ("Ancestor0", "Ancestor1"),
    ("Ancestor0", "Elephant"),
    ("Ancestor1", "Ancestor2"),
    ("Ancestor1", "Ancestor3"),
    ("Ancestor2", "Dog"),
    ("Ancestor2", "Cat"),
    ("Ancestor3", "Mouse"),
    ("Ancestor3", "Rat"),
]

labels = {
    "Ancestor0": "AGC",
    "Ancestor1": "AGC",
    "Elephant": "GGC",
    "Ancestor2": "TGC",
    "Ancestor3": "AGC",
    "Dog": "AGC",
    "Cat": "TGC",
    "Mouse": "AGC",
    "Rat": "CGC",
}

for ancestor, node, position, pattern in reversing_substitutions(edges, labels):
    print(ancestor, node, position, pattern)
