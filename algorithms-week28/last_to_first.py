def last_to_first(last_column, i):
    ranks = [0] * len(last_column)
    seen = {}
    for idx, char in enumerate(last_column):
        seen[char] = seen.get(char, 0) + 1
        ranks[idx] = seen[char]

    first_column = sorted(last_column)
    target_char = last_column[i]
    target_rank = ranks[i]

    count = 0
    for idx, char in enumerate(first_column):
        if char == target_char:
            count += 1
            if count == target_rank:
                return idx

last_column = "T$GACCA"
i = 3

print(last_to_first(last_column, i))
