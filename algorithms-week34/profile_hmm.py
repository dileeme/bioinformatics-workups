def build_states(match_count):
    states = ["S", "I0"]
    for i in range(1, match_count + 1):
        states += [f"M{i}", f"D{i}", f"I{i}"]
    states.append("E")
    return states

def profile_hmm(theta, alphabet, alignment):
    n_seqs = len(alignment)
    ncols = len(alignment[0])
    gap = "-"

    gap_frac = [sum(1 for row in alignment if row[c] == gap) / n_seqs for c in range(ncols)]
    match_cols = {c for c in range(ncols) if gap_frac[c] < theta}
    match_count = len(match_cols)

    states = build_states(match_count)
    transition_counts = {s: {t: 0 for t in states} for s in states}
    emission_states = [s for s in states if s not in ("S", "E") and not s.startswith("D")]
    emission_counts = {s: {a: 0 for a in alphabet} for s in emission_states}

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

    return states, transition, emission

def print_matrix(states, table, columns):
    print("\t" + "\t".join(columns))
    for s in states:
        print(s + "\t" + "\t".join(f"{table[s][c]:.3f}" for c in columns))

theta = 0.5
alphabet = ["A", "B", "C", "D", "E"]
alignment = ["ACA-A", "AC-AA", "AC--A", "AC-DA", "AC-EA"]

states, transition, emission = profile_hmm(theta, alphabet, alignment)

print_matrix(states, transition, states)
print("--------")
print_matrix(states, emission, alphabet)
