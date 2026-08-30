from collections import deque

def parse_newick(text):
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
        while pos[0] < len(s) and s[pos[0]] not in ",()":
            pos[0] += 1
        return s[start:pos[0]]

    def parse_clade():
        if s[pos[0]] == "(":
            pos[0] += 1
            node = make_node()
            while True:
                child = parse_clade()
                edges.append((node, child))
                if s[pos[0]] == ",":
                    pos[0] += 1
                    continue
                if s[pos[0]] == ")":
                    pos[0] += 1
                    break
            parse_label()
            return node
        else:
            label = parse_label()
            node = make_node()
            leaf_id[label] = node
            return node

    parse_clade()
    return edges, leaf_id

def tree_distance(text, a, b):
    edges, leaf_id = parse_newick(text)
    adjacency = {}
    for u, v in edges:
        adjacency.setdefault(u, []).append(v)
        adjacency.setdefault(v, []).append(u)

    start = leaf_id[a]
    target = leaf_id[b]
    visited = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return visited[node]
        for neighbor in adjacency.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    return -1

queries = [
    ("(dog,cat);", "dog", "cat"),
    ("(dog,cat,(mouse,rat));", "mouse", "rat"),
]

results = [tree_distance(tree, a, b) for tree, a, b in queries]
print(" ".join(str(r) for r in results))
