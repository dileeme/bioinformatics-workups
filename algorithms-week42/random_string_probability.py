from math import log10

def log_probability(s, gc_content):
    log_prob = 0.0
    for base in s:
        if base in "GC":
            p = gc_content / 2
        else:
            p = (1 - gc_content) / 2
        log_prob += log10(p)
    return log_prob

s = "ACGATACAA"
gc_contents = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]

print(" ".join(f"{log_probability(s, gc):.3f}" for gc in gc_contents))
