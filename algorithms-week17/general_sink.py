def general_sink(n, edges):
    radj = [[] for _ in range(n + 1)]
    for u, v in edges:
        radj[v].append(u)

    def reaches_all(candidate):
        visited = {candidate}
        stack = [candidate]
        while stack:
            node = stack.pop()
            for neighbor in radj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return len(visited) == n

    for candidate in range(1, n + 1):
        if reaches_all(candidate):
            return candidate
    return -1

graphs = [
    (3, [(1, 2), (2, 3)]),
    (4, [(1, 2), (3, 4)]),
]

print(" ".join(str(general_sink(n, edges)) for n, edges in graphs))
