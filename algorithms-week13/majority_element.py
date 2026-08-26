def majority_element(a):
    candidate = None
    count = 0
    for x in a:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    if a.count(candidate) > len(a) // 2:
        return candidate
    return -1

arrays = [
    [5, 5, 5, 5, 5, 5, 5, 5],
    [8, 7, 7, 7, 5, 7, 8, 7],
    [7, 1, 6, 5, 10, 100, 1000, 1],
    [5, 1, 6, 7, 1, 1, 10, 1],
]

print(" ".join(str(majority_element(a)) for a in arrays))
