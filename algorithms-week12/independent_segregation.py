import math

def log_at_least_k(n):
    trials = 2 * n
    results = []
    for k in range(1, trials + 1):
        prob = sum(
            math.comb(trials, i) * (0.5 ** trials)
            for i in range(k, trials + 1)
        )
        results.append(math.log10(prob))
    return results

n = 1

print(" ".join(f"{v:.3f}" for v in log_at_least_k(n)))
