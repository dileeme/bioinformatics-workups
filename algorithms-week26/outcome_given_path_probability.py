def outcome_probability(outcome, path, emission):
    prob = 1.0
    for symbol, state in zip(outcome, path):
        prob *= emission[state][symbol]
    return prob

outcome = "xyx"
path = "AAB"

emission = {
    "A": {"x": 0.5, "y": 0.5},
    "B": {"x": 0.2, "y": 0.8},
}

print(outcome_probability(outcome, path, emission))
