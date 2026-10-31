def generate_ordered_strings(alphabet, max_length):
    result = []

    def recurse(prefix):
        if prefix:
            result.append(prefix)
        if len(prefix) == max_length:
            return
        for symbol in alphabet:
            recurse(prefix + symbol)

    recurse("")
    return result

alphabet = ["D", "N", "A"]
max_length = 3

for s in generate_ordered_strings(alphabet, max_length):
    print(s)
