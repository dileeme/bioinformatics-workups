def cycle_to_chromosome(nodes):
    chromosome = []
    for j in range(len(nodes) // 2):
        a, b = nodes[2 * j], nodes[2 * j + 1]
        if a < b:
            chromosome.append(b // 2)
        else:
            chromosome.append(-(a // 2))
    return chromosome

def format_chromosome(chromosome):
    return " ".join(f"+{block}" if block > 0 else str(block) for block in chromosome)

nodes = [1, 2, 4, 3, 6, 5, 7, 8]

print(format_chromosome(cycle_to_chromosome(nodes)))
