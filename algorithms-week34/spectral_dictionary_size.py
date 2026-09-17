from collections import Counter

integer_mass = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "I": 113, "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128,
    "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
}

def spectral_dictionary_size(spectral_vector, threshold, max_score):
    m = len(spectral_vector)
    masses = list(integer_mass.values())
    size = [Counter() for _ in range(m + 1)]
    size[0][0] = 1
    for i in range(1, m + 1):
        for mass in masses:
            if i - mass >= 0:
                for score, count in size[i - mass].items():
                    size[i][score + spectral_vector[i - 1]] += count
    return sum(count for score, count in size[m].items() if threshold <= score <= max_score)

spectral_vector = [((i * 37) % 11) - 5 for i in range(1, 201)]
threshold = -3
max_score = 5

print(spectral_dictionary_size(spectral_vector, threshold, max_score))
