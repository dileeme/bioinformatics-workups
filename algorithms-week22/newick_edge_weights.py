from collections import deque

def parse_weighted_newick(text):
    s = text.strip()
    if s.endswith(";"):
        s = s[:-1]
    pos = [0]
    edges = []
    leaf_id = {}
    next_id = [0]

    def make_node():
        next_id[0] += 1
        return next_id[0]

    def parse_label():
        start = pos[0]
        while pos[0] < len(s) and s[pos[0]] not in ",():;":
            pos[0] += 1
        return s[start:pos[0]]

    def parse_weight():
        if pos[0] < len(s) and s[pos[0]] == ":":
            pos[0] += 1
            start = pos[0]
            while pos[0] < len(s) and s[pos[0]] not in ",();":
                pos[0] += 1
            return float(s[start:pos[0]])
        return None

    def parse_clade():
        if s[pos[0]] == "(":
            pos[0] += 1
            node = make_node()
            while True:
                child, weight = parse_clade()
                edges.append((node, child, weight))
                if s[pos[0]] == ",":
                    pos[0] += 1
                    continue
                if s[pos[0]] == ")":
                    pos[0] += 1
                    break
            parse_label()
            return node, parse_weight()
        else:
            label = parse_label()
            node = make_node()
            leaf_id[label] = node
            return node, parse_weight()

    root, _ = parse_clade()
    return root, edges, leaf_id

def tree_distance(text, a, b):
    _, edges, leaf_id = parse_weighted_newick(text)
    adjacency = {}
    for u, v, w in edges:
        adjacency.setdefault(u, []).append((v, w))
        adjacency.setdefault(v, []).append((u, w))

    start = leaf_id[a]
    target = leaf_id[b]
    visited = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return visited[node]
        for neighbor, weight in adjacency.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = visited[node] + weight
                queue.append(neighbor)
    return -1

queries = [
    ("(dog:42,cat:33);", "dog", "cat"),
    ("((dog:4,cat:3):2,weasel:20);", "dog", "weasel"),
]

results = [tree_distance(tree, a, b) for tree, a, b in queries]
print(" ".join(str(int(r)) for r in results))
