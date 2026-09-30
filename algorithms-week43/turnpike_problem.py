from collections import Counter

def place(remaining, points, width):
    if not remaining:
        return True

    y = max(remaining)
    for candidate in (y, width - y):
        if candidate in points:
            continue

        diffs = Counter(abs(candidate - x) for x in points)
        if any(remaining[d] < c for d, c in diffs.items()):
            continue

        for d, c in diffs.items():
            remaining[d] -= c
            if remaining[d] == 0:
                del remaining[d]
        points.add(candidate)

        if place(remaining, points, width):
            return True

        points.discard(candidate)
        for d, c in diffs.items():
            remaining[d] += c

    return False

def reconstruct_points(distances):
    remaining = Counter(distances)
    width = max(remaining)
    del remaining[width]
    points = {0, width}

    place(remaining, points, width)
    return sorted(points)

distances = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]

points = reconstruct_points(distances)
print(" ".join(str(p) for p in points))
