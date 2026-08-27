def count_inversions(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2
    left, left_inv = count_inversions(a[:mid])
    right, right_inv = count_inversions(a[mid:])

    merged = []
    i = j = inv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, left_inv + right_inv + inv

a = [-6, 1, 15, 8, 10, 3]

_, total = count_inversions(a)
print(total)
