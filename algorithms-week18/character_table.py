import re
from collections import defaultdict

def parse_newick(text):
    text = text.strip().rstrip(";")
    tokens = re.findall(r"[(),]|[^(),]+", text)

    nodes = []
    edges = []

    def new_node():
        nodes.append(len(nodes))
        return nodes[-1]

    root = new_node()
    stack = [root]
    i = 0
    while i < len(tokens):
        tok = tokens[i]
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
        i += 1
    return root, edges

leaves = {}

def leaves_on_side(edges, u, v, all_leaf_ids):
    adj = defaultdict(list)
    for a, b in edges:
        if (a, b) == (u, v) or (a, b) == (v, u):
            continue
        adj[a].append(b)
        adj[b].append(a)
    visited = {u}
    stack = [u]
    while stack:
        node = stack.pop()
        for nb in adj[node]:
            if nb not in visited:
                visited.add(nb)
                stack.append(nb)
    return visited & all_leaf_ids

newick = "(A,(B,C),(D,(E,F)));"
root, edges = parse_newick(newick)
species = sorted(leaves.values())
leaf_ids = {node: name for node, name in leaves.items()}
all_leaf_ids = set(leaf_ids.keys())

for u, v in edges:
    side = leaves_on_side(edges, u, v, all_leaf_ids)
    if 1 < len(side) < len(species) - 1:
        names_on_side = {leaf_ids[node] for node in side}
        print("".join("1" if name in names_on_side else "0" for name in species))
