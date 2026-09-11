def squared_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))

def nearest_center(point, centers):
    return min(range(len(centers)), key=lambda i: squared_distance(point, centers[i]))

def centroid(points):
    m = len(points)
    dims = len(points[0])
    return tuple(sum(p[d] for p in points) / m for d in range(dims))

def lloyd_kmeans(points, k):
    centers = points[:k]
    while True:
        clusters = [[] for _ in range(k)]
        for point in points:
            clusters[nearest_center(point, centers)].append(point)

        new_centers = [centroid(cluster) if cluster else centers[i] for i, cluster in enumerate(clusters)]

        if new_centers == centers:
            break
        centers = new_centers

    return centers

k = 2
points = [
    (1.3, 1.1), (1.3, 0.2), (0.6, 2.8), (3.0, 3.2), (1.2, 0.7),
    (1.4, 1.6), (1.2, 1.0), (1.2, 1.1), (0.6, 1.5), (1.8, 2.6),
    (1.2, 1.3), (1.2, 1.0), (0.0, 1.9),
]

for center in lloyd_kmeans(points, k):
    print(" ".join(f"{c:.3f}" for c in center))
