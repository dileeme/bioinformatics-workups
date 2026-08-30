def remove_distances(multiset, values):
    remaining = list(multiset)
    for v in values:
        remaining.remove(v)
    return remaining

def place(multiset, points, width):
    if not multiset:
        return points
    y = max(multiset)
    for candidate in (y, width - y):
        needed = sorted(abs(candidate - x) for x in points)
        if all(needed.count(v) <= multiset.count(v) for v in set(needed)):
            new_multiset = remove_distances(multiset, needed)
            result = place(new_multiset, points + [candidate], width)
            if result is not None:
                return result
    return None

def partial_digest(distances):
    multiset = list(distances)
    width = max(multiset)
    multiset.remove(width)
    points = [0, width]
    result = place(multiset, points, width)
    return sorted(result)

distances = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]

print(" ".join(str(p) for p in partial_digest(distances)))
