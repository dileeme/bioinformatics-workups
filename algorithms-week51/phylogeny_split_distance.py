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
            return ("internal", children)
        start = pos[0]
        while pos[0] < len(s) and s[pos[0]] not in ",()":
            pos[0] += 1
        return ("leaf", s[start:pos[0]])

    return parse_clade()

def all_leaves(node):
    if node[0] == "leaf":
        return {node[1]}
    leaves = set()
    for child in node[1]:
        leaves |= all_leaves(child)
    return leaves

def collect_splits(node, anchor, universe, splits, is_root):
    if node[0] == "leaf":
        return {node[1]}
    subtree_leaves = set()
    for child in node[1]:
        subtree_leaves |= collect_splits(child, anchor, universe, splits, False)
    if not is_root:
        side = subtree_leaves if anchor not in subtree_leaves else universe - subtree_leaves
        if 2 <= len(side) <= len(universe) - 2:
            splits.add(frozenset(side))
    return subtree_leaves

def nontrivial_splits(newick):
    tree = parse_newick(newick)
    universe = all_leaves(tree)
    anchor = min(universe)
    splits = set()
    collect_splits(tree, anchor, universe, splits, True)
    return splits

def split_distance(newick_a, newick_b):
    splits_a = nontrivial_splits(newick_a)
    splits_b = nontrivial_splits(newick_b)
    return len(splits_a ^ splits_b)

tree_a = "((A,B),(C,D),E);"
tree_b = "((A,B),(C,E),D);"

print(split_distance(tree_a, tree_b))
