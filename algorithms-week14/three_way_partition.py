def three_way_partition(a):
    pivot = a[0]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return less + equal + greater

a = [7, 2, 5, 6, 1, 3, 9, 5, 6, 8, 5, 4]

print(" ".join(str(x) for x in three_way_partition(a)))
