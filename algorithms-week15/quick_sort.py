def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [x for x in a[1:] if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a[1:] if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

a = [7, 2, 5, 3, 9, 4, 6, 1, 8]

print(" ".join(str(x) for x in quick_sort(a)))
