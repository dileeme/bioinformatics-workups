def partial_sort(values, k):
    values = list(values)
    n = len(values)
    for i in range(min(k, n)):
        min_index = i
        for j in range(i + 1, n):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
    return values[:k]

values = [5, -2, 4, 7, 5, 3, 5, -3, 1, 2]
k = 3

print(" ".join(str(v) for v in partial_sort(values, k)))
