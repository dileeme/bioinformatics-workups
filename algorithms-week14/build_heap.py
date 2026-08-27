def sift_down(a, i, n):
    while True:
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
        if largest == i:
            break
        a[i], a[largest] = a[largest], a[i]
        i = largest

def build_max_heap(a):
    a = a[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(a, i, n)
    return a

a = [4, 5, 8, 2, 6, 7, 3, 1, 9]

print(" ".join(str(x) for x in build_max_heap(a)))
