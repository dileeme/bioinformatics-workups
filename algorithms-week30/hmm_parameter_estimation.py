def estimate_parameters(x, alphabet, path, states):
    transition_counts = {a: {b: 0 for b in states} for a in states}
    emission_counts = {a: {b: 0 for b in alphabet} for a in states}

    for i in range(len(path)):
        emission_counts[path[i]][x[i]] += 1
        if i + 1 < len(path):
            transition_counts[path[i]][path[i + 1]] += 1

    transition = {}
    for state in states:
        total = sum(transition_counts[state].values())
        if total == 0:
            transition[state] = {b: 1 / len(states) for b in states}
        else:
            transition[state] = {b: transition_counts[state][b] / total for b in states}

    emission = {}
    for state in states:
        total = sum(emission_counts[state].values())
        if total == 0:
            emission[state] = {b: 1 / len(alphabet) for b in alphabet}
        else:
            emission[state] = {b: emission_counts[state][b] / total for b in alphabet}

    return transition, emission

x = "AABBAABA"
alphabet = ["A", "B"]
path = "HHLLHHLH"
states = ["H", "L"]

transition, emission = estimate_parameters(x, alphabet, path, states)

print("\t" + "\t".join(states))
for a in states:
    print(a + "\t" + "\t".join(f"{transition[a][b]:.3f}" for b in states))

print("--------")
print("\t" + "\t".join(alphabet))
for a in states:
    print(a + "\t" + "\t".join(f"{emission[a][b]:.3f}" for b in alphabet))
