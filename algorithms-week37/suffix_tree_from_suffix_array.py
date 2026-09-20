def suffix_tree_from_sa(text, sa, lcp):
    n = len(text)
    edge_label = {}
    children = {}
    next_id = [1]
    stack = [(0, 0)]

    for i in range(n):
        depth = lcp[i] if i > 0 else 0
        last_popped = None
        while stack[-1][1] > depth:
            last_popped = stack.pop()
        if stack[-1][1] < depth:
            parent_node, parent_depth = stack[-1]
            child_node, _ = last_popped
            label = edge_label[(parent_node, child_node)]
            split_len = depth - parent_depth
            new_node = next_id[0]
            next_id[0] += 1
            del edge_label[(parent_node, child_node)]
            children[parent_node].remove(child_node)
            edge_label[(parent_node, new_node)] = label[:split_len]
            children.setdefault(parent_node, []).append(new_node)
            edge_label[(new_node, child_node)] = label[split_len:]
            children.setdefault(new_node, []).append(child_node)
            stack.append((new_node, depth))

        parent_node, _ = stack[-1]
        leaf = next_id[0]
        next_id[0] += 1
        suffix_start = sa[i]
        edge_label[(parent_node, leaf)] = text[suffix_start + depth:]
        children.setdefault(parent_node, []).append(leaf)
        stack.append((leaf, n - suffix_start))

    return list(edge_label.values())

text = "panamabananas$"
suffix_array = [13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10, 0, 12]
lcp_array = [0, 0, 1, 1, 3, 3, 1, 0, 0, 0, 2, 2, 0, 0]

for edge in suffix_tree_from_sa(text, suffix_array, lcp_array):
    print(edge)
