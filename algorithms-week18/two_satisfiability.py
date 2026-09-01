def lit_index(lit):
    return 2 * (lit - 1) if lit > 0 else 2 * (-lit - 1) + 1

def neg_index(idx):
    return idx ^ 1

def solve_2sat(n, clauses):
    size = 2 * n
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]
    for a, b in clauses:
        ia, ib = lit_index(a), lit_index(b)
        adj[neg_index(ia)].append(ib)
        radj[ib].append(neg_index(ia))
        adj[neg_index(ib)].append(ia)
        radj[ia].append(neg_index(ib))

    visited = [False] * size
    order = []

    def dfs1(start):
        stack = [(start, iter(adj[start]))]
        visited[start] = True
        while stack:
            node, it = stack[-1]
            advanced = False
            for neighbor in it:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, iter(adj[neighbor])))
                    advanced = True
                    break
            if not advanced:
                order.append(node)
                stack.pop()

    for v in range(size):
        if not visited[v]:
            dfs1(v)

    comp = [-1] * size
    comp_id = 0

    def dfs2(start, cid):
        stack = [start]
        comp[start] = cid
        while stack:
            node = stack.pop()
            for neighbor in radj[node]:
                if comp[neighbor] == -1:
                    comp[neighbor] = cid
                    stack.append(neighbor)

    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, comp_id)
            comp_id += 1

    assignment = [None] * (n + 1)
    for i in range(1, n + 1):
        pos, neg = lit_index(i), lit_index(-i)
        if comp[pos] == comp[neg]:
            return None
        assignment[i] = comp[pos] > comp[neg]

    return assignment[1:]

test_cases = [
    (3, [(1, -2), (2, 3), (-1, -3), (1, 2)]),
    (1, [(1, 1), (-1, -1)]),
]

for n, clauses in test_cases:
    result = solve_2sat(n, clauses)
    if result is None:
        print(0)
    else:
        print(" ".join(str(i + 1) if v else str(-(i + 1)) for i, v in enumerate(result)))
