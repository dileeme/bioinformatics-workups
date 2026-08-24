import math

def log_probabilities(s, gc_contents):
    results = []
    for gc in gc_contents:
        log_prob = 0.0
        for base in s:
            if base in "GC":
                log_prob += math.log10(gc / 2)
            else:
                log_prob += math.log10((1 - gc) / 2)
        results.append(log_prob)
    return results

s = "ACGATACAA"
gc_contents = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]

print(" ".join(f"{p:.3f}" for p in log_probabilities(s, gc_contents)))
