import math

def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def soft_kmeans(points, k, beta, iterations, seed_centers):
    centers = [list(c) for c in seed_centers]
    dimensions = len(points[0])

    for _ in range(iterations):
        responsibilities = []
        for point in points:
            weights = [math.exp(-beta * distance(point, center)) for center in centers]
            total = sum(weights)
            responsibilities.append([weight / total for weight in weights])

        new_centers = []
        for cluster in range(k):
            weight_sum = sum(responsibilities[i][cluster] for i in range(len(points)))
            new_center = [
                sum(responsibilities[i][cluster] * points[i][d] for i in range(len(points))) / weight_sum
                for d in range(dimensions)
            ]
            new_centers.append(new_center)
        centers = new_centers

    return centers

points = [
    [3.0, 5.0], [1.0, 4.5], [1.5, 10.0], [4.0, 9.0],
    [7.0, 5.0], [8.0, 4.0], [9.0, 6.0], [5.0, 3.0],
]
k = 2
beta = 1.0
seed_centers = [points[0], points[4]]

centers = soft_kmeans(points, k, beta, 100, seed_centers)
for center in centers:
    print(" ".join(f"{value:.3f}" for value in center))
