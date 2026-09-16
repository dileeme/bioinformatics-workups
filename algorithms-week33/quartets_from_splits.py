from itertools import combinations

def resolved_quartets(taxa, splits):
    taxa_set = set(taxa)
    quartets = set()
    for side_a in splits:
        side_a = set(side_a)
        side_b = taxa_set - side_a
        for a_pair in combinations(sorted(side_a), 2):
            for b_pair in combinations(sorted(side_b), 2):
                left = tuple(sorted(a_pair))
                right = tuple(sorted(b_pair))
                quartets.add(tuple(sorted([left, right])))
    return sorted(quartets)

taxa = ["A", "B", "C", "D", "E"]
splits = [["A", "B"], ["A", "B", "C"]]

for left, right in resolved_quartets(taxa, splits):
    print(" ".join(left) + " | " + " ".join(right))
