from itertools import combinations

def inferred_quartets(taxa, splits):
    results = []
    for quartet in combinations(taxa, 4):
        quartet_set = set(quartet)
        for split in splits:
            on_side = quartet_set & split
            if len(on_side) == 2:
                other_side = quartet_set - on_side
                results.append((frozenset(on_side), frozenset(other_side)))
                break
    return results

taxa = ["cat", "dog", "elephant", "mouse", "rabbit"]
splits = [
    frozenset({"cat", "dog"}),
    frozenset({"cat", "dog", "elephant"}),
]

for a, b in inferred_quartets(taxa, splits):
    print(" ".join(sorted(a)), "|", " ".join(sorted(b)))
