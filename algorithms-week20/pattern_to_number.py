def pattern_to_number(pattern):
    order = {"A": 0, "C": 1, "G": 2, "T": 3}
    number = 0
    for base in pattern:
        number = number * 4 + order[base]
    return number

pattern = "AGT"

print(pattern_to_number(pattern))
