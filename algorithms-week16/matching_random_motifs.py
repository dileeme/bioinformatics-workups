def motif_probability(motif, gc_content):
    probability = 1.0
    for base in motif:
        if base in "GC":
            probability *= gc_content / 2
        else:
            probability *= (1 - gc_content) / 2
    return probability

def at_least_one_match(n, gc_content, motif):
    p = motif_probability(motif, gc_content)
    return 1 - (1 - p) ** n

n = 90000
gc_content = 0.6
motif = "ATAGCCGA"

print(f"{at_least_one_match(n, gc_content, motif) + 1e-9:.3f}")
