def chromosome_to_cycle(chromosome):
    nodes = []
    for block in chromosome:
        if block > 0:
            nodes.append(2 * block - 1)
            nodes.append(2 * block)
        else:
            nodes.append(-2 * block)
            nodes.append(-2 * block - 1)
    return nodes

def format_cycle(nodes):
    return "(" + " ".join(str(n) for n in nodes) + ")"

chromosome = [1, -2, -3]

print(format_cycle(chromosome_to_cycle(chromosome)))
