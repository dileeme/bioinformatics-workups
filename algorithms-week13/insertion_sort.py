def count_insertion_swaps(a):
    a = a[:]
    swaps = 0
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
            swaps += 1
    return swaps

n = 6
a = [6, 10, 4, 5, 1, 2]

print(count_insertion_swaps(a))
