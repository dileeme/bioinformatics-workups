def build_character_table(strings):
    n = len(strings)
    length = len(strings[0])
    table = []

    for pos in range(length):
        column = [s[pos] for s in strings]
        reference = column[0]
        bits = "".join("0" if c == reference else "1" for c in column)
        ones = bits.count("1")
        if 2 <= ones <= n - 2:
            table.append(bits)

    return table

strings = [
    "ATGCAT",
    "ATGCAT",
    "ATCCAT",
    "GTCCAC",
    "GTCTAT",
]

for row in build_character_table(strings):
    print(row)
