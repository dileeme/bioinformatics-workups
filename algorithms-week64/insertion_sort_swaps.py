def count_insertion_sort_swaps(arr):
    arr = arr[:]
    swaps = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            swaps += 1
    return swaps

array = [6, 10, 4, 5, 1, 2]

print(count_insertion_sort_swaps(array))
