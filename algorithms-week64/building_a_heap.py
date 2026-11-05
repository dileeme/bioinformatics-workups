def build_max_heap(arr):
    arr = arr[:]
    n = len(arr)

    def sift_down(i):
        while True:
            largest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest == i:
                break
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)
    return arr

array = [4, 5, 3, 2, 1, 9, 6, 8, 7]

print(" ".join(str(x) for x in build_max_heap(array)))
