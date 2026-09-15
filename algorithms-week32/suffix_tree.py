def build_trie(s):
    children = [{}]
    for i in range(len(s)):
        cur = 0
        for c in s[i:]:
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

s = "ATAAATG$"

children = build_trie(s)
edges = compressed_edges(children)

for edge in edges:
    print(edge)
