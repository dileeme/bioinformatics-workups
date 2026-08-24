def mortal_rabbits(n, m):
    cohorts = [1] + [0] * (m - 1)
    for _ in range(n - 1):
        newborns = sum(cohorts[1:])
        cohorts = [newborns] + cohorts[:-1]
    return sum(cohorts)

n = 6
m = 3

print(mortal_rabbits(n, m))
