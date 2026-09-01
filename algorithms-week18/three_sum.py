def find_zero_triples(arr):
    n = len(arr)
    indexed = sorted(range(n), key=lambda i: arr[i])
    for pos, i in enumerate(indexed):
        lo, hi = pos + 1, n - 1
        while lo < hi:
            j, k = indexed[lo], indexed[hi]
            total = arr[i] + arr[j] + arr[k]
            if total == 0:
                return sorted([i + 1, j + 1, k + 1])
            elif total < 0:
                lo += 1
            else:
                hi -= 1
    return None

arrays = [
    [2, -3, 0, 1, -5],
    [1, 4, -5, -3, 3],
    [1, 2, 3, 4, 5],
]

for arr in arrays:
    result = find_zero_triples(arr)
    if result is None:
        print(-1)
    else:
        print(" ".join(str(x) for x in result))
