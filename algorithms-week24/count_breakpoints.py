def count_breakpoints(perm):
    extended = [0] + perm + [len(perm) + 1]
    breakpoints = 0
    for i in range(len(extended) - 1):
        if extended[i + 1] - extended[i] != 1:
            breakpoints += 1
    return breakpoints

perm = [3, 4, 5, -12, -8, -7, -6, 1, 2, 10, 9, -11]

print(count_breakpoints(perm))
