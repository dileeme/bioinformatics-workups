def forward_matrix(x, states, transition, emission):
    n = len(x)
    forward = [{} for _ in range(n)]
    for state in states:
        forward[0][state] = (1 / len(states)) * emission[state][x[0]]
    for i in range(1, n):
        for state in states:
            total = sum(forward[i - 1][prev] * transition[prev][state] for prev in states)
            forward[i][state] = total * emission[state][x[i]]
    return forward

def backward_matrix(x, states, transition, emission):
    n = len(x)
    backward = [{} for _ in range(n)]
    for state in states:
        backward[n - 1][state] = 1.0
    for i in range(n - 2, -1, -1):
        for state in states:
            backward[i][state] = sum(
                transition[state][nxt] * emission[nxt][x[i + 1]] * backward[i + 1][nxt]
                for nxt in states
            )
    return backward

def baum_welch_iteration(x, alphabet, states, transition, emission):
    n = len(x)
    forward = forward_matrix(x, states, transition, emission)
    backward = backward_matrix(x, states, transition, emission)
    px = sum(forward[n - 1].values())

    gamma = [{state: forward[i][state] * backward[i][state] / px for state in states} for i in range(n)]

    xi_sum = {k: {l: 0.0 for l in states} for k in states}
    for i in range(n - 1):
        for k in states:
            for l in states:
                xi_sum[k][l] += forward[i][k] * transition[k][l] * emission[l][x[i + 1]] * backward[i + 1][l] / px

    gamma_excl_last = {k: sum(gamma[i][k] for i in range(n - 1)) for k in states}
    new_transition = {
        k: {l: xi_sum[k][l] / gamma_excl_last[k] for l in states}
        for k in states
    }

    gamma_all = {k: sum(gamma[i][k] for i in range(n)) for k in states}
    new_emission = {}
    for k in states:
        new_emission[k] = {
            b: sum(gamma[i][k] for i in range(n) if x[i] == b) / gamma_all[k]
            for b in alphabet
        }

    return new_transition, new_emission

def baum_welch_learning(x, alphabet, states, transition, emission, iterations):
    for _ in range(iterations):
        transition, emission = baum_welch_iteration(x, alphabet, states, transition, emission)
    return transition, emission

x = "xzyyzzyzyyzz"
alphabet = ["x", "y", "z"]
states = ["A", "B"]
transition = {"A": {"A": 0.5, "B": 0.5}, "B": {"A": 0.5, "B": 0.5}}
emission = {"A": {"x": 0.4, "y": 0.3, "z": 0.3}, "B": {"x": 0.2, "y": 0.3, "z": 0.5}}
iterations = 10

transition, emission = baum_welch_learning(x, alphabet, states, transition, emission, iterations)

print("\t" + "\t".join(states))
for a in states:
    print(a + "\t" + "\t".join(f"{transition[a][b]:.4f}" for b in states))

print("--------")
print("\t" + "\t".join(alphabet))
for a in states:
    print(a + "\t" + "\t".join(f"{emission[a][b]:.4f}" for b in alphabet))
