def outcome_probability(outcome, states, transition, emission):
    forward = {state: (1.0 / len(states)) * emission[state][outcome[0]] for state in states}

    for symbol in outcome[1:]:
        new_forward = {}
        for state in states:
            total = sum(forward[prev] * transition[prev][state] for prev in states)
            new_forward[state] = total * emission[state][symbol]
        forward = new_forward

    return sum(forward.values())

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

print(outcome_probability(outcome, states, transition, emission))
