def squared_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))

def squared_error_distortion(centers, points):
    total = sum(min(squared_distance(point, center) for center in centers) for point in points)
    return total / len(points)

centers = [(2.31, 4.55), (5.96, 9.08)]
points = [
    (3.42, 6.03), (6.23, 8.25), (4.76, 1.64), (4.47, 4.33),
    (3.95, 7.61), (8.93, 2.97), (9.53, 7.28), (1.06, 5.75),
    (3.54, 8.48), (6.58, 9.07),
]

print(round(squared_error_distortion(centers, points), 3))
