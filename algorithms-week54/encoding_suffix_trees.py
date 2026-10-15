def build_trie(s):
    children = [{}]
    start_pos = {}
    for i in range(len(s)):
        cur = 0
        for k, c in enumerate(s[i:]):
            if c not in children[cur]:
                children.append({})
                children[cur][c] = len(children) - 1
                start_pos[(cur, children[cur][c])] = i + k
            cur = children[cur][c]
    return children, start_pos

def encoded_edges(children, start_pos):
    edges = []

    def dfs(node):
        for c, child in children[node].items():
            length = 1
            start = start_pos[(node, child)]
            cur = child
            while len(children[cur]) == 1:
                (next_char, next_node), = children[cur].items()
                length += 1
                cur = next_node
            edges.append((length, start))
            dfs(cur)

    dfs(0)
    return edges

s = "ATAAATG$"

children, start_pos = build_trie(s)

for length, start in encoded_edges(children, start_pos):
    print(length, start)
