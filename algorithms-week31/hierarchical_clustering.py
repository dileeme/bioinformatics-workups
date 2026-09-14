def hierarchical_clustering(matrix, n):
    size = {i: 1 for i in range(1, n + 1)}
    distance = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                distance[(i, j)] = matrix[i - 1][j - 1]

    active = set(range(1, n + 1))
    next_id = n + 1
    merges = []

    while len(active) > 1:
        best_pair = None
        best_distance = None
        for i in active:
            for j in active:
                if i < j and (best_distance is None or distance[(i, j)] < best_distance):
                    best_distance = distance[(i, j)]
                    best_pair = (i, j)

        i, j = best_pair
        merges.append(best_pair)
        merged_size = size[i] + size[j]

        for k in active:
            if k != i and k != j:
                new_distance = (distance[(i, k)] * size[i] + distance[(j, k)] * size[j]) / merged_size
                distance[(next_id, k)] = new_distance
                distance[(k, next_id)] = new_distance

        active.discard(i)
        active.discard(j)
        active.add(next_id)
        size[next_id] = merged_size
        next_id += 1

    return merges

matrix = [
    [0, 2, 9, 10],
    [2, 0, 8, 9],
    [9, 8, 0, 3],
    [10, 9, 3, 0],
]

for i, j in hierarchical_clustering(matrix, 4):
    print(i, j)
