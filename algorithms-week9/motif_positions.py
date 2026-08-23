def find_motif(s, t):
    positions = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(i + 1)
    return positions

s = "GATATATGCATATACTT"
t = "ATAT"

print(" ".join(str(p) for p in find_motif(s, t)))
