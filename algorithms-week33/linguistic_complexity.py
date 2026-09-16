def linguistic_complexity(s):
    n = len(s)
    total_possible = 0
    total_distinct = 0
    for length in range(1, n + 1):
        total_possible += min(4 ** length, n - length + 1)
        total_distinct += len(set(s[i:i + length] for i in range(n - length + 1)))
    return total_distinct / total_possible

s = "ATTTGGATT"

print(f"{linguistic_complexity(s):.5f}")
