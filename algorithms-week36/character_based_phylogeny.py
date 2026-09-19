def build_subtree(taxa, splits, counter):
    if len(taxa) == 1:
        return next(iter(taxa)), []

    chosen = None
    for split in splits:
        overlap = split & taxa
        if overlap and overlap != taxa:
            chosen = overlap
            break

    if chosen is None:
        node_id = "N" + str(counter[0])
        counter[0] += 1
        edges = [(node_id, taxon) for taxon in sorted(taxa)]
        return node_id, edges

    remaining = taxa - chosen
    left_label, left_edges = build_subtree(chosen, splits, counter)
    right_label, right_edges = build_subtree(remaining, splits, counter)
    node_id = "N" + str(counter[0])
    counter[0] += 1
    edges = left_edges + right_edges + [(node_id, left_label), (node_id, right_label)]
    return node_id, edges

def build_unrooted_tree(taxa, splits):
    counter = [0]
    chosen = None
    for split in splits:
        overlap = split & taxa
        if overlap and overlap != taxa:
            chosen = overlap
            break
    remaining = taxa - chosen
    left_label, left_edges = build_subtree(chosen, splits, counter)
    right_label, right_edges = build_subtree(remaining, splits, counter)
    return left_edges + right_edges + [(left_label, right_label)]

taxa = {"A", "B", "C", "D"}
splits = [frozenset({"A", "B"})]

edges = build_unrooted_tree(taxa, splits)
for node1, node2 in edges:
    print(node1, node2)
