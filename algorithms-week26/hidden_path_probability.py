def hidden_path_probability(path, states, transition):
    prob = 1.0 / len(states)
    for i in range(1, len(path)):
        prob *= transition[path[i - 1]][path[i]]
    return prob

path = "ABA"

states = ["A", "B"]
transition = {
    "A": {"A": 0.3, "B": 0.7},
    "B": {"A": 0.4, "B": 0.6},
}

print(hidden_path_probability(path, states, transition))
