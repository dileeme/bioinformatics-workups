def viterbi(x, states, transition, emission, initial):
    n = len(x)
    scores = [{} for _ in range(n)]
    backptr = [{} for _ in range(n)]

    for state in states:
        scores[0][state] = initial[state] * emission[state][x[0]]
        backptr[0][state] = None

    for i in range(1, n):
        for state in states:
            best_prev, best_score = None, -1
            for prev in states:
                candidate = scores[i - 1][prev] * transition[prev][state]
                if candidate > best_score:
                    best_score, best_prev = candidate, prev
            scores[i][state] = best_score * emission[state][x[i]]
            backptr[i][state] = best_prev

    last_state = max(states, key=lambda state: scores[n - 1][state])
    path = [last_state]
    for i in range(n - 1, 0, -1):
        path.append(backptr[i][path[-1]])
    path.reverse()
    return "".join(path)

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

def viterbi_learning(x, alphabet, states, transition, emission, iterations):
    initial = {state: 1 / len(states) for state in states}
    for _ in range(iterations):
        path = viterbi(x, states, transition, emission, initial)
        transition, emission = estimate_parameters(x, alphabet, path, states)
    return transition, emission

x = "AAABBBAAABBB"
alphabet = ["A", "B"]
states = ["H", "L"]
transition = {"H": {"H": 0.5, "L": 0.5}, "L": {"H": 0.5, "L": 0.5}}
emission = {"H": {"A": 0.6, "B": 0.4}, "L": {"A": 0.4, "B": 0.6}}

transition, emission = viterbi_learning(x, alphabet, states, transition, emission, 10)

print("\t" + "\t".join(states))
for a in states:
    print(a + "\t" + "\t".join(f"{transition[a][b]:.3f}" for b in states))

print("--------")
print("\t" + "\t".join(alphabet))
for a in states:
    print(a + "\t" + "\t".join(f"{emission[a][b]:.3f}" for b in alphabet))
