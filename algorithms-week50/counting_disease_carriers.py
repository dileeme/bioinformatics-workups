from math import sqrt

def carrier_frequency(k):
    q = sqrt(k)
    p = 1 - q
    return 2 * p * q

frequencies = [0.1, 0.25, 0.5]

print(" ".join(f"{carrier_frequency(k):.3f}" for k in frequencies))
