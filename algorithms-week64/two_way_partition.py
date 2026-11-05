def partition(arr):
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater_equal = [x for x in arr[1:] if x >= pivot]
    return less + [pivot] + greater_equal

array = [7, 2, 5, 6, 1, 3, 9, 4, 8]

print(" ".join(str(x) for x in partition(array)))
