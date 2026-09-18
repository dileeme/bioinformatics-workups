import math

def build_states(match_count):
    states = ["S", "I0"]
    for i in range(1, match_count + 1):
        states += [f"M{i}", f"D{i}", f"I{i}"]
    states.append("E")
    return states

def valid_next_states(state, match_count):
    if state in ("S", "I0"):
        return ["I0", "M1", "D1"]
    level = int(state[1:])
    if level < match_count:
        return [f"I{level}", f"M{level + 1}", f"D{level + 1}"]
    return [f"I{level}", "E"]

def profile_hmm_with_pseudocounts(theta, sigma, alphabet, alignment):
    n_seqs = len(alignment)
    ncols = len(alignment[0])
    gap = "-"

    gap_frac = [sum(1 for row in alignment if row[c] == gap) / n_seqs for c in range(ncols)]
    match_cols = {c for c in range(ncols) if gap_frac[c] < theta}
    match_count = len(match_cols)

    states = build_states(match_count)
    transition_counts = {s: {t: 0.0 for t in states} for s in states}
    emission_states = [s for s in states if s not in ("S", "E") and not s.startswith("D")]
    emission_counts = {s: {a: 0.0 for a in alphabet} for s in emission_states}

    for row in alignment:
        path = ["S"]
        match_idx = 0
        for c in range(ncols):
            ch = row[c]
            if c in match_cols:
                match_idx += 1
                if ch == gap:
                    path.append(f"D{match_idx}")
                else:
                    path.append(f"M{match_idx}")
                    emission_counts[f"M{match_idx}"][ch] += 1
            elif ch != gap:
                path.append(f"I{match_idx}")
                emission_counts[f"I{match_idx}"][ch] += 1
        path.append("E")
        for a, b in zip(path, path[1:]):
            transition_counts[a][b] += 1

    for s in states:
        if s == "E":
            continue
        for t in valid_next_states(s, match_count):
            transition_counts[s][t] += sigma

    for s in emission_states:
        for a in alphabet:
            emission_counts[s][a] += sigma

    transition = {}
    for s in states:
        total = sum(transition_counts[s].values())
        transition[s] = {t: (transition_counts[s][t] / total if total > 0 else 0.0) for t in states}

    emission = {}
    for s in states:
        if s in emission_counts:
            total = sum(emission_counts[s].values())
            emission[s] = {a: (emission_counts[s][a] / total if total > 0 else 0.0) for a in alphabet}
        else:
            emission[s] = {a: 0.0 for a in alphabet}

    return transition, emission, match_count

NEG_INF = float("-inf")

def log(x):
    return math.log(x) if x > 0 else NEG_INF

def align_to_profile_hmm(text, transition, emission, match_count):
    n = len(text)
    L = match_count

    VM = [[NEG_INF] * (L + 1) for _ in range(n + 1)]
    VD = [[NEG_INF] * (L + 1) for _ in range(n + 1)]
    VI = [[NEG_INF] * (L + 1) for _ in range(n + 1)]
    BM = [[None] * (L + 1) for _ in range(n + 1)]
    BD = [[None] * (L + 1) for _ in range(n + 1)]
    BI = [[None] * (L + 1) for _ in range(n + 1)]

    VS = 0.0

    for i in range(n + 1):
        if i >= 1:
            candidates = []
            if i - 1 == 0:
                candidates.append((VS + log(transition["S"]["I0"]), ("S", None)))
            candidates.append((VI[i - 1][0] + log(transition["I0"]["I0"]), ("I", 0)))
            best_score, best_from = max(candidates, key=lambda x: x[0])
            VI[i][0] = best_score + log(emission["I0"][text[i - 1]])
            BI[i][0] = best_from

        for k in range(1, L + 1):
            if i >= 1:
                candidates = []
                if k == 1:
                    if i - 1 == 0:
                        candidates.append((VS + log(transition["S"]["M1"]), ("S", None)))
                    candidates.append((VI[i - 1][0] + log(transition["I0"]["M1"]), ("I", 0)))
                else:
                    candidates.append((VM[i - 1][k - 1] + log(transition[f"M{k - 1}"][f"M{k}"]), ("M", k - 1)))
                    candidates.append((VD[i - 1][k - 1] + log(transition[f"D{k - 1}"][f"M{k}"]), ("D", k - 1)))
                    candidates.append((VI[i - 1][k - 1] + log(transition[f"I{k - 1}"][f"M{k}"]), ("I", k - 1)))
                best_score, best_from = max(candidates, key=lambda x: x[0])
                VM[i][k] = best_score + log(emission[f"M{k}"][text[i - 1]])
                BM[i][k] = best_from

                candidates = [
                    (VM[i - 1][k] + log(transition[f"M{k}"][f"I{k}"]), ("M", k)),
                    (VD[i - 1][k] + log(transition[f"D{k}"][f"I{k}"]), ("D", k)),
                    (VI[i - 1][k] + log(transition[f"I{k}"][f"I{k}"]), ("I", k)),
                ]
                best_score, best_from = max(candidates, key=lambda x: x[0])
                VI[i][k] = best_score + log(emission[f"I{k}"][text[i - 1]])
                BI[i][k] = best_from

            candidates = []
            if k == 1:
                if i == 0:
                    candidates.append((VS + log(transition["S"]["D1"]), ("S", None)))
                if i >= 1:
                    candidates.append((VI[i][0] + log(transition["I0"]["D1"]), ("I", 0)))
            else:
                candidates.append((VM[i][k - 1] + log(transition[f"M{k - 1}"][f"D{k}"]), ("M", k - 1)))
                candidates.append((VD[i][k - 1] + log(transition[f"D{k - 1}"][f"D{k}"]), ("D", k - 1)))
                candidates.append((VI[i][k - 1] + log(transition[f"I{k - 1}"][f"D{k}"]), ("I", k - 1)))
            if candidates:
                best_score, best_from = max(candidates, key=lambda x: x[0])
                VD[i][k] = best_score
                BD[i][k] = best_from

    final_candidates = [
        (VM[n][L] + log(transition[f"M{L}"]["E"]), ("M", L)),
        (VD[n][L] + log(transition[f"D{L}"]["E"]), ("D", L)),
        (VI[n][L] + log(transition[f"I{L}"]["E"]), ("I", L)),
    ]
    state_type, k = max(final_candidates, key=lambda x: x[0])[1]

    path = []
    i = n
    while state_type != "S":
        if state_type == "M":
            path.append(f"M{k}")
            prev_type, prev_k = BM[i][k]
            i -= 1
        elif state_type == "I":
            path.append("I0" if k == 0 else f"I{k}")
            prev_type, prev_k = BI[i][k]
            i -= 1
        else:
            path.append(f"D{k}")
            prev_type, prev_k = BD[i][k]
        state_type, k = prev_type, prev_k
    path.reverse()
    return path

theta = 0.35
sigma = 0.01
alphabet = ["A", "B"]
alignment = ["ABA", "AB-", "A-A", "ABA"]
text = "AAB"

transition, emission, match_count = profile_hmm_with_pseudocounts(theta, sigma, alphabet, alignment)
path = align_to_profile_hmm(text, transition, emission, match_count)

print(" ".join(path))
