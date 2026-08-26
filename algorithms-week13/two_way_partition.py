def partition(a):
    a = a[:]
    pivot = a[0]
    i = 0
    for j in range(1, len(a)):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[0], a[i] = a[i], a[0]
    return a

a = [5, 2, 5, 5, 8, 5, 3, 9, 5]

print(" ".join(str(x) for x in partition(a)))
