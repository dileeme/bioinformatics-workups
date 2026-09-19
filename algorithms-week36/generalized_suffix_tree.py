def build_trie(strings):
    children = [{}]
    for s in strings:
        cur = 0
        for c in s:
            if c not in children[cur]:
                children.append({})
                children[cur][c] = len(children) - 1
            cur = children[cur][c]
    return children

def compressed_edges(children):
    edges = []

    def dfs(node):
        for c, child in children[node].items():
            label = c
            cur = child
            while len(children[cur]) == 1:
                (next_char, next_node), = children[cur].items()
                label += next_char
                cur = next_node
            edges.append(label)
            dfs(cur)

    dfs(0)
    return edges

def generalized_suffix_tree(s, t):
    suffixes = [s[i:] + "#" for i in range(len(s))] + [t[j:] + "$" for j in range(len(t))]
    children = build_trie(suffixes)
    return compressed_edges(children)

s = "AB"
t = "BA"

for edge in generalized_suffix_tree(s, t):
    print(edge)
