def merge_sorted(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

a = [2, 4, 10, 18, 20, 25]
b = [1, 3, 9, 11, 12, 13, 14]

print(" ".join(str(x) for x in merge_sorted(a, b)))
