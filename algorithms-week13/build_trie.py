def build_trie(patterns):
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

for u, v, char in build_trie(patterns):
    print(u, v, char)
