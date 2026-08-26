def binary_search(a, key):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == key:
            return mid + 1
        elif a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

a = [10, 20, 30, 40, 50]
keys = [40, 10, 35, 15, 40, 20]

print(" ".join(str(binary_search(a, key)) for key in keys))
