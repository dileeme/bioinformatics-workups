def degree_array(n, edges):
    degrees = [0] * (n + 1)
    for a, b in edges:
        degrees[a] += 1
        degrees[b] += 1
    return degrees[1:]

n = 6
edges = [(1, 2), (2, 3), (6, 3), (5, 6), (2, 5), (2, 4), (4, 1)]

print(" ".join(str(d) for d in degree_array(n, edges)))
