def build_trie(patterns):
    children = {0: {}}
    next_node = 1

    for pattern in patterns:
        current = 0
        for char in pattern:
            if char in children[current]:
                current = children[current][char]
            else:
                children[current][char] = next_node
                children[next_node] = {}
                current = next_node
                next_node += 1

    return children

def prefix_trie_matching(text, trie):
    node = 0
    for char in text:
        if char not in trie[node]:
            return not trie[node]
        node = trie[node][char]
        if not trie[node]:
            return True
    return not trie[node]

def trie_matching(text, patterns):
    trie = build_trie(patterns)
    positions = []
    for i in range(len(text)):
        if prefix_trie_matching(text[i:], trie):
            positions.append(i)
    return positions

text = "AATCGGGTTCAATCGGGGT"
patterns = ["ATCG", "GGGT"]

print(" ".join(str(p) for p in trie_matching(text, patterns)))
