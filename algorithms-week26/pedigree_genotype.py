GENOTYPES = ["AA", "Aa", "aa"]
ALLELES = {"AA": ["A", "A"], "Aa": ["A", "a"], "aa": ["a", "a"]}

def cross(genotype_a, genotype_b):
    result = {g: 0.0 for g in GENOTYPES}
    for allele_a in ALLELES[genotype_a]:
        for allele_b in ALLELES[genotype_b]:
            pair = sorted([allele_a, allele_b], key=lambda a: a != "A")
            offspring = "".join(pair)
            result[offspring] += 0.25
    return result

def combine(dist_a, dist_b):
    result = {g: 0.0 for g in GENOTYPES}
    for genotype_a, prob_a in dist_a.items():
        for genotype_b, prob_b in dist_b.items():
            offspring_dist = cross(genotype_a, genotype_b)
            for genotype, prob in offspring_dist.items():
                result[genotype] += prob_a * prob_b * prob
    return result

def parse_node(text, pos):
    if text[pos] == "(":
        pos += 1
        left, pos = parse_node(text, pos)
        pos += 1
        right, pos = parse_node(text, pos)
        pos += 1
        return ("internal", left, right), pos
    start = pos
    while text[pos] not in ",()":
        pos += 1
    return ("leaf", text[start:pos]), pos

def evaluate(node):
    if node[0] == "leaf":
        return {g: (1.0 if g == node[1] else 0.0) for g in GENOTYPES}
    _, left, right = node
    return combine(evaluate(left), evaluate(right))

def pedigree_probabilities(newick):
    tree = newick.strip().rstrip(";")
    root, _ = parse_node(tree, 0)
    distribution = evaluate(root)
    return [distribution[g] for g in GENOTYPES]

newick = "((AA,Aa),(Aa,aa));"

print(" ".join(f"{p:.3f}" for p in pedigree_probabilities(newick)))
