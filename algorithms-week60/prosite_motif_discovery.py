import re

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

def prosite_to_regex(pattern):
    tokens = pattern.strip().rstrip(".").split("-")
    regex_parts = []
    for token in tokens:
        match = re.match(r"^x\((\d+)(?:,(\d+))?\)$", token)
        if match:
            low = match.group(1)
            high = match.group(2)
            regex_parts.append(f".{{{low},{high}}}" if high else f".{{{low}}}")
        elif token == "x":
            regex_parts.append(".")
        elif token.startswith("{") and token.endswith("}"):
            regex_parts.append(f"[^{token[1:-1]}]")
        elif token.startswith("[") and token.endswith("]"):
            regex_parts.append(f"[{token[1:-1]}]")
        else:
            regex_parts.append(re.escape(token))
    return "".join(regex_parts)

def find_motif_positions(sequence, pattern):
    regex = prosite_to_regex(pattern)
    positions = []
    for i in range(len(sequence)):
        if re.match(regex, sequence[i:]):
            positions.append(i + 1)
    return positions

fasta = """
>Rosalind_11
MTCCASKAGHRTDAESDFYAQ
>Rosalind_22
MSTVDEAKLMNRSTIDEFGHP
>Rosalind_33
MKASTGDEPLRASTLDELQNR
"""

pattern = "[ST]-x(2)-[DE]"

sequences = parse_fasta(fasta)

for label, sequence in sequences.items():
    positions = find_motif_positions(sequence, pattern)
    if positions:
        print(label)
        print(" ".join(str(p) for p in positions))
