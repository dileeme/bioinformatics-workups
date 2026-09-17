def soft_decode(outcome, states, transition, emission):
    n = len(outcome)

    forward = [{} for _ in range(n)]
    for state in states:
        forward[0][state] = (1 / len(states)) * emission[state][outcome[0]]
    for i in range(1, n):
        for state in states:
            total = sum(forward[i - 1][prev] * transition[prev][state] for prev in states)
            forward[i][state] = total * emission[state][outcome[i]]

    backward = [{} for _ in range(n)]
    for state in states:
        backward[n - 1][state] = 1.0
    for i in range(n - 2, -1, -1):
        for state in states:
            backward[i][state] = sum(
                transition[state][nxt] * emission[nxt][outcome[i + 1]] * backward[i + 1][nxt]
                for nxt in states
            )

    px = sum(forward[n - 1].values())
    return [{state: forward[i][state] * backward[i][state] / px for state in states} for i in range(n)]

outcome = "xzyyzzyzyy"
states = ["A", "B"]
transition = {
    "A": {"A": 0.303, "B": 0.697},
    "B": {"A": 0.831, "B": 0.169},
}
emission = {
    "A": {"x": 0.533, "y": 0.065, "z": 0.402},
    "B": {"x": 0.342, "y": 0.334, "z": 0.324},
}

posterior = soft_decode(outcome, states, transition, emission)

print("\t".join(states))
for row in posterior:
    print("\t".join(f"{row[state]:.4f}" for state in states))
