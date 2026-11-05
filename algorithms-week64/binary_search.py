def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

array = [10, 20, 30, 40, 50]
queries = [40, 10, 35, 15, 40, 20]

print(" ".join(str(binary_search(array, q)) for q in queries))
