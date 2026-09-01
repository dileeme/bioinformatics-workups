from collections import deque

def sorting_by_reversals(perm):
    n = len(perm)
    identity = tuple(range(1, n + 1))
    if perm == identity:
        return []

    parent = {perm: (None, None)}
    queue = deque([perm])
    while queue:
        current = queue.popleft()
        for i in range(n):
            for j in range(i + 1, n):
                candidate = current[:i] + current[i:j + 1][::-1] + current[j + 1:]
                if candidate not in parent:
                    parent[candidate] = (current, (i, j))
                    if candidate == identity:
                        queue.clear()
                        break
                    queue.append(candidate)
            else:
                continue
            break

    steps = []
    node = identity
    while parent[node][0] is not None:
        prev, move = parent[node]
        steps.append(move)
        node = prev
    steps.reverse()
    return steps

perm = (3, 1, 5, 2, 7, 4, 8, 6)
reversals = sorting_by_reversals(perm)

print(len(reversals))
for i, j in reversals:
    print(i + 1, j + 1)
