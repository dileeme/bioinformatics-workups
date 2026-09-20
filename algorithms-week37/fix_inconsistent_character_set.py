from itertools import combinations

def conflicts(c1, c2):
    pairs = set(zip(c1, c2))
    return {("1", "1"), ("1", "0"), ("0", "1"), ("0", "0")} <= pairs

def find_conflicting_pair(characters):
    for i, j in combinations(range(len(characters)), 2):
        if conflicts(characters[i], characters[j]):
            return i, j
    return None

def fix_conflict(characters, i, j):
    c1 = list(characters[i])
    groups = {("1", "1"): [], ("1", "0"): [], ("0", "1"): [], ("0", "0"): []}
    for idx, (a, b) in enumerate(zip(c1, characters[j])):
        groups[(a, b)].append(idx)
    smallest_key = min(groups, key=lambda k: len(groups[k]))
    a_val, _ = smallest_key
    for idx in groups[smallest_key]:
        c1[idx] = "0" if a_val == "1" else "1"
    fixed = list(characters)
    fixed[i] = "".join(c1)
    return fixed

characters = [
    "110000",
    "111000",
    "001110",
]

i, j = find_conflicting_pair(characters)
fixed_characters = fix_conflict(characters, i, j)

for character in fixed_characters:
    print(character)
