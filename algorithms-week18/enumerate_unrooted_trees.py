from collections import defaultdict

def insert_leaf_round(trees, leaf_id, new_node_id):
    new_trees = []
    for edges in trees:
        for e in edges:
            u, v = e
            remaining = [x for x in edges if x != e]
            new_trees.append(remaining + [(u, new_node_id), (v, new_node_id), (leaf_id, new_node_id)])
    return new_trees

def generate_unrooted_trees(n):
    root = n
    trees = [[(0, root), (1, root), (2, root)]]
    next_internal = root + 1
    for leaf in range(3, n):
        trees = insert_leaf_round(trees, leaf, next_internal)
        next_internal += 1
    return trees

def to_newick(edges, species, root):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def build(node, parent):
        neighbors = [nb for nb in adj[node] if nb != parent]
        if not neighbors:
            return species[node]
        return "(" + ",".join(build(nb, node) for nb in neighbors) + ")"

    return build(root, None) + ";"

species = ["dog", "cat", "mouse", "elephant"]
n = len(species)

for edges in generate_unrooted_trees(n):
    print(to_newick(edges, species, n))
