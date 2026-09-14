import re
from collections import defaultdict

def parse_newick(text):
    text = text.strip().rstrip(";")
    tokens = re.findall(r"[(),]|[^(),]+", text)
    edges = []
    leaves = {}
    counter = [0]

    def new_node():
        counter[0] += 1
        return counter[0]

    root = new_node()
    stack = [root]
    for tok in tokens:
        if tok == "(":
            child = new_node()
            edges.append((stack[-1], child))
            stack.append(child)
        elif tok == ",":
            stack.pop()
            child = new_node()
            edges.append((stack[-1], child))
            stack.append(child)
        elif tok == ")":
            stack.pop()
        else:
            leaves[stack[-1]] = tok
    return edges, leaves

def side_leaves(edges, u, v, leaves):
    adjacency = defaultdict(list)
    for a, b in edges:
        if (a, b) == (u, v) or (a, b) == (v, u):
            continue
        adjacency[a].append(b)
        adjacency[b].append(a)
    visited = {u}
    stack = [u]
    while stack:
        node = stack.pop()
        for neighbor in adjacency[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return {leaves[n] for n in visited if n in leaves}

def non_trivial_splits(text):
    edges, leaves = parse_newick(text)
    all_names = set(leaves.values())
    reference = min(all_names)
    splits = set()
    for u, v in edges:
        side = side_leaves(edges, u, v, leaves)
        if 1 < len(side) < len(all_names) - 1:
            if reference in side:
                side = all_names - side
            splits.add(frozenset(side))
    return splits

def split_distance(tree1, tree2):
    splits1 = non_trivial_splits(tree1)
    splits2 = non_trivial_splits(tree2)
    return len(splits1 - splits2) + len(splits2 - splits1)

tree1 = "(A,B,(C,(D,E)));"
tree2 = "(A,C,(B,(D,E)));"

print(split_distance(tree1, tree2))
