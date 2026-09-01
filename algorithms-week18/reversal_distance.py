from collections import deque

def reversal_distance(start, target):
    if start == target:
        return 0
    n = len(start)
    seen = {start}
    queue = deque([(start, 0)])
    while queue:
        perm, dist = queue.popleft()
        for i in range(n):
            for j in range(i + 1, n):
                candidate = perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]
                if candidate == target:
                    return dist + 1
                if candidate not in seen:
                    seen.add(candidate)
                    queue.append((candidate, dist + 1))
    return -1

pairs = [
    ((1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 6, 7, 8)),
    ((1, 2, 3, 4, 5, 6, 7, 8), (8, 7, 6, 5, 4, 3, 2, 1)),
    ((3, 1, 5, 2, 7, 4, 8, 6), (1, 2, 3, 4, 5, 6, 7, 8)),
]

print(" ".join(str(reversal_distance(a, b)) for a, b in pairs))
