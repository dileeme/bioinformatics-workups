def parse_newick(text):
    s = text.strip().rstrip(";")
    pos = [0]

    def parse_clade():
        if s[pos[0]] == "(":
            pos[0] += 1
            children = [parse_clade()]
            while s[pos[0]] == ",":
                pos[0] += 1
                children.append(parse_clade())
            pos[0] += 1
            label = parse_label()
            return ("internal", children, label)
        label = parse_label()
        return ("leaf", label)

    def parse_label():
        start = pos[0]
        while pos[0] < len(s) and s[pos[0]] not in ",()":
            pos[0] += 1
        return s[start:pos[0]]

    return parse_clade()

def build_edges(node):
    edges = []
    counter = [0]

    def assign(node):
        if node[0] == "leaf":
            return node[1]
        name = node[2] if node[2] else f"__internal{counter[0]}"
        counter[0] += 1
        for child in node[1]:
            child_name = assign(child)
            edges.append((name, child_name))
        return name

    root_name = assign(node)
    return edges, root_name

def unroot(edges, root_name):
    root_children = [v for u, v in edges if u == root_name] + [u for u, v in edges if v == root_name]
    if len(root_children) == 2:
        edges = [e for e in edges if root_name not in e]
        edges.append((root_children[0], root_children[1]))
    return edges

def tree_distance(newick, a, b):
    tree = parse_newick(newick)
    edges, root_name = build_edges(tree)
    edges = unroot(edges, root_name)

    adjacency = {}
    for u, v in edges:
        adjacency.setdefault(u, []).append(v)
        adjacency.setdefault(v, []).append(u)

    visited = {a: 0}
    queue = [a]
    while queue:
        node = queue.pop(0)
        if node == b:
            return visited[node]
        for neighbor in adjacency.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    return -1

queries = [
    ("(cat)dog;", "dog", "cat"),
    ("((dog,cat),mouse);", "dog", "mouse"),
]

print(" ".join(str(tree_distance(newick, a, b)) for newick, a, b in queries))
