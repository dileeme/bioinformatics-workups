import math

def viterbi_path(outcome, states, transition, emission):
    n = len(outcome)
    scores = [{} for _ in range(n)]
    backpointer = [{} for _ in range(n)]

    for state in states:
        scores[0][state] = math.log(1.0 / len(states)) + math.log(emission[state][outcome[0]])

    for i in range(1, n):
        for state in states:
            best_prev, best_score = None, float("-inf")
            for prev in states:
                score = scores[i - 1][prev] + math.log(transition[prev][state])
                if score > best_score:
                    best_score, best_prev = score, prev
            scores[i][state] = best_score + math.log(emission[state][outcome[i]])
            backpointer[i][state] = best_prev

    last_state = max(states, key=lambda state: scores[n - 1][state])
    path = [last_state]
    for i in range(n - 1, 0, -1):
        last_state = backpointer[i][last_state]
        path.append(last_state)
    path.reverse()

    return "".join(path)

outcome = "xyyx"
states = ["A", "B"]

transition = {
    "A": {"A": 0.6, "B": 0.4},
    "B": {"A": 0.3, "B": 0.7},
}

emission = {
    "A": {"x": 0.7, "y": 0.3},
    "B": {"x": 0.2, "y": 0.8},
}

print(viterbi_path(outcome, states, transition, emission))
