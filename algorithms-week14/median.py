import random

def quickselect(a, k):
    pivot = random.choice(a)
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]

    if k <= len(less):
        return quickselect(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        return quickselect(greater, k - len(less) - len(equal))

a = [8, 5, 12, 15, 4, 9, 13, 3, 11, 7]
k = 5

print(quickselect(a, k))
