def first_occurrence(first_column):
    first_occ = {}
    for idx, char in enumerate(first_column):
        if char not in first_occ:
            first_occ[char] = idx
    return first_occ

def count_symbol(last_column, symbol, position):
    return last_column[:position].count(symbol)

def bw_matching(last_column, pattern):
    first_column = sorted(last_column)
    first_occ = first_occurrence(first_column)

    top, bottom = 0, len(last_column) - 1
    pattern = list(pattern)
    while top <= bottom:
        if pattern:
            symbol = pattern.pop()
            window = last_column[top:bottom + 1]
            if symbol in window:
                top = first_occ[symbol] + count_symbol(last_column, symbol, top)
                bottom = first_occ[symbol] + count_symbol(last_column, symbol, bottom + 1) - 1
            else:
                return 0
        else:
            return bottom - top + 1
    return 0

last_column = "TCCTCTATGAGATCCTATTCTATGAAAGCTGCTCTAGGA$"
patterns = ["CCT", "CAC", "GAG", "CAGA"]

print(" ".join(str(bw_matching(last_column, pattern)) for pattern in patterns))
