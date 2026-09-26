def build_trie(s):
    children = [{}]
    origin = {}
    for i in range(len(s)):
        cur = 0
        d = 0
        for c in s[i:]:
            if c not in children[cur]:
                children.append({})
                new_node = len(children) - 1
                children[cur][c] = new_node
                origin[new_node] = (i, d)
            cur = children[cur][c]
            d += 1
    return children, origin

def encode_suffix_tree(s):
    children, origin = build_trie(s)
    edges = []

    def dfs(node):
        for child in children[node].values():
            i, d = origin[child]
            length = 1
            cur = child
            while len(children[cur]) == 1:
                cur = next(iter(children[cur].values()))
                length += 1
            edges.append((i + d, length))
            dfs(cur)

    dfs(0)
    return edges

s = "ATAAATG$"

for start, length in encode_suffix_tree(s):
    print(start, length)
