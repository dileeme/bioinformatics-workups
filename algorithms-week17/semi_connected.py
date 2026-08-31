def component_ids(n, edges):
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)

    visited = [False] * (n + 1)
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

    for v in range(1, n + 1):
        if not visited[v]:
            dfs1(v)

    comp = [0] * (n + 1)
    label = 0

    def dfs2(start, label):
        stack = [start]
        comp[start] = label
        while stack:
            node = stack.pop()
            for neighbor in radj[node]:
                if comp[neighbor] == 0:
                    comp[neighbor] = label
                    stack.append(neighbor)

    for v in reversed(order):
        if comp[v] == 0:
            label += 1
            dfs2(v, label)

    return comp, label

def is_semi_connected(n, edges):
    comp, num_components = component_ids(n, edges)
    cond_adj = [set() for _ in range(num_components + 1)]
    in_degree = [0] * (num_components + 1)
    for u, v in edges:
        if comp[u] != comp[v] and comp[v] not in cond_adj[comp[u]]:
            cond_adj[comp[u]].add(comp[v])
            in_degree[comp[v]] += 1

    queue = [c for c in range(1, num_components + 1) if in_degree[c] == 0]
    topo = []
    while queue:
        queue.sort()
        node = queue.pop(0)
        topo.append(node)
        for neighbor in cond_adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    for i in range(len(topo) - 1):
        if topo[i + 1] not in cond_adj[topo[i]]:
            return False
    return True

graphs = [
    (3, [(1, 2), (2, 3)]),
    (4, [(1, 2), (3, 4)]),
]

print(" ".join("1" if is_semi_connected(n, edges) else "-1" for n, edges in graphs))
