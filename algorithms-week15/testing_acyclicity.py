def is_acyclic(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * (n + 1)

    def has_cycle(start):
        stack = [(start, iter(adj[start]))]
        color[start] = GRAY
        while stack:
            node, it = stack[-1]
            advanced = False
            for neighbor in it:
                if color[neighbor] == GRAY:
                    return True
                if color[neighbor] == WHITE:
                    color[neighbor] = GRAY
                    stack.append((neighbor, iter(adj[neighbor])))
                    advanced = True
                    break
            if not advanced:
                color[node] = BLACK
                stack.pop()
        return False

    for v in range(1, n + 1):
        if color[v] == WHITE:
            if has_cycle(v):
                return False
    return True

graphs = [
    (4, [(1, 2), (2, 3), (3, 4)]),
    (3, [(1, 2), (2, 3), (3, 1)]),
]

print(" ".join("1" if is_acyclic(n, edges) else "-1" for n, edges in graphs))
