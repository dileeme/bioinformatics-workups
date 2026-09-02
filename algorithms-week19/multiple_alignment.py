from itertools import product

def parse_fasta(text):
    sequences = {}
    label = None
    for line in text.strip().splitlines():
        if line.startswith(">"):
            label = line[1:].strip()
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return sequences

def column_score(chars):
    return 0 if len(set(chars)) == 1 and "-" not in chars else -1

def multiple_alignment(strings):
    lengths = [len(s) for s in strings]
    dp = {}
    parent = {}
    dp[(0, 0, 0, 0)] = 0

    ranges = [range(lengths[k] + 1) for k in range(4)]
    for state in product(*ranges):
        if state == (0, 0, 0, 0):
            continue
        best_score, best_move = None, None
        for mask in range(1, 16):
            prev = list(state)
            ok = True
            chars = []
            for k in range(4):
                if mask & (1 << k):
                    prev[k] -= 1
                    if prev[k] < 0:
                        ok = False
                        break
                    chars.append(strings[k][prev[k]])
                else:
                    chars.append("-")
            if not ok:
                continue
            prev_state = tuple(prev)
            if prev_state not in dp:
                continue
            score = dp[prev_state] + column_score(chars)
            if best_score is None or score > best_score:
                best_score, best_move = score, (prev_state, mask)
        dp[state] = best_score
        parent[state] = best_move

    final_state = tuple(lengths)
    aligned = [[] for _ in range(4)]
    state = final_state
    while state != (0, 0, 0, 0):
        prev_state, mask = parent[state]
        for k in range(4):
            if mask & (1 << k):
                aligned[k].append(strings[k][prev_state[k]])
            else:
                aligned[k].append("-")
        state = prev_state

    return dp[final_state], ["".join(reversed(a)) for a in aligned]

fasta = """
>Rosalind_1
ACGT
>Rosalind_2
ACT
>Rosalind_3
AT
>Rosalind_4
AGT
"""

sequences = parse_fasta(fasta)
strings = list(sequences.values())

score, alignment = multiple_alignment(strings)

print(score)
for line in alignment:
    print(line)
