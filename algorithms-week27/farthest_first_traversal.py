def distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def farthest_first_traversal(points, k):
    centers = [points[0]]
    while len(centers) < k:
        farthest, farthest_dist = None, -1
        for point in points:
            nearest = min(distance(point, center) for center in centers)
            if nearest > farthest_dist:
                farthest, farthest_dist = point, nearest
        centers.append(farthest)
    return centers

k = 3
points = [
    (0.0, 0.0),
    (5.0, 5.0),
    (0.0, 5.0),
    (1.0, 1.0),
    (2.0, 2.0),
    (3.0, 3.0),
    (1.0, 2.0),
]

for center in farthest_first_traversal(points, k):
    print(" ".join(str(c) for c in center))
