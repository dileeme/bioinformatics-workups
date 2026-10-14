def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = 693, 609

print(gcd(a, b))
