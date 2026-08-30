def base_probability(base, gc_content):
    if base in "GC":
        return gc_content / 2
    return (1 - gc_content) / 2

def expected_occurrences(n, motif, gc_content):
    site_probability = 1.0
    for base in motif:
        site_probability *= base_probability(base, gc_content)
    positions = n - len(motif) + 1
    return positions * site_probability

n = 10
motif = "AG"
gc_contents = [0.25, 0.5, 0.75]

results = [expected_occurrences(n, motif, gc) for gc in gc_contents]
print(" ".join(f"{value + 1e-9:.3f}" for value in results))
