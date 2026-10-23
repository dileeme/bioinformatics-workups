import bisect

def longest_monotonic_subsequence(sequence, increasing=True):
    if not increasing:
        sequence = [-x for x in sequence]

    tails = []
    tail_indices = []
    predecessors = [-1] * len(sequence)

    for i, value in enumerate(sequence):
        pos = bisect.bisect_left(tails, value)
        if pos == len(tails):
            tails.append(value)
            tail_indices.append(i)
        else:
            tails[pos] = value
            tail_indices[pos] = i
        predecessors[i] = tail_indices[pos - 1] if pos > 0 else -1

    subsequence = []
    k = tail_indices[-1]
    while k != -1:
        subsequence.append(k)
        k = predecessors[k]
    subsequence.reverse()

    original = sequence if increasing else [-x for x in sequence]
    return [original[i] for i in subsequence]

permutation = [5, 1, 4, 2, 3]

increasing = longest_monotonic_subsequence(permutation, increasing=True)
decreasing = longest_monotonic_subsequence(permutation, increasing=False)

print(" ".join(map(str, increasing)))
print(" ".join(map(str, decreasing)))
