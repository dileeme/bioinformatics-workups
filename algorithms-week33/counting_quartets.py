from itertools import combinations
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

    root = parse_clade()
    return root, edges, leaf_id

def unroot_edges(root, edges):
    adjacency = {}
    for u, v in edges:
        adjacency.setdefault(u, []).append(v)
        adjacency.setdefault(v, []).append(u)
    root_children = adjacency.get(root, [])
    if len(root_children) == 2:
        a, b = root_children
        new_edges = [(u, v) for u, v in edges if root not in (u, v)]
        new_edges.append((a, b))
        return new_edges
    return edges

def bfs_distances(adjacency, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in adjacency.get(node, []):
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

def count_resolved_quartets(text):
    root, edges, leaf_id = parse_newick(text)
    edges = unroot_edges(root, edges)
    adjacency = {}
    for u, v in edges:
        adjacency.setdefault(u, []).append(v)
        adjacency.setdefault(v, []).append(u)

    names = list(leaf_id.keys())
    dist = {name: bfs_distances(adjacency, leaf_id[name]) for name in names}

    count = 0
    for a, b, c, d in combinations(names, 4):
        pairings = [
            dist[a][leaf_id[b]] + dist[c][leaf_id[d]],
            dist[a][leaf_id[c]] + dist[b][leaf_id[d]],
            dist[a][leaf_id[d]] + dist[b][leaf_id[c]],
        ]
        smallest, second = sorted(pairings)[:2]
        if smallest < second:
            count += 1
    return count

tree = "(((dog,cat),horse),(mouse,rat),(cow,pig));"

print(count_resolved_quartets(tree))
