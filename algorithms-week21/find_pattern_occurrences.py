def find_occurrences(pattern, genome):
    k = len(pattern)
    return [i for i in range(len(genome) - k + 1) if genome[i:i + k] == pattern]

pattern = "ATAT"
genome = "GATATATGCATATACTT"

print(" ".join(str(i) for i in find_occurrences(pattern, genome)))
