def trie_construction(patterns):
    children = {1: {}}
    edges = []
    next_node = 2

    for pattern in patterns:
        current = 1
        for char in pattern:
            if char in children[current]:
                current = children[current][char]
            else:
                children[current][char] = next_node
                children[next_node] = {}
                edges.append((current, next_node, char))
                current = next_node
                next_node += 1

    return edges

patterns = ["ATAGA", "ATC", "GAT"]

for parent, child, char in trie_construction(patterns):
    print(f"{parent}->{child}:{char}")
