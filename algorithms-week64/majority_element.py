from collections import Counter

def majority_element(arr):
    value, count = Counter(arr).most_common(1)[0]
    if count > len(arr) // 2:
        return value
    return -1

arrays = [
    [1, 2, 3, 2, 2, 2, 5],
    [1, 2, 3, 4, 5, 6, 7],
    [9, 9, 9, 9, 1, 2, 9],
]

print(" ".join(str(majority_element(a)) for a in arrays))
