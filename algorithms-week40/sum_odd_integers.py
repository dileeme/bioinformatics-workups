def sum_odd_integers(a, b):
    return sum(n for n in range(a, b + 1) if n % 2 == 1)

a, b = 100, 200

print(sum_odd_integers(a, b))
