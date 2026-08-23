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

def reverse_complement(dna):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(dna))

def find_reverse_palindromes(dna, min_len=4, max_len=12):
    sites = []
    for length in range(min_len, max_len + 1, 2):
        for i in range(len(dna) - length + 1):
            substring = dna[i:i + length]
            if substring == reverse_complement(substring):
                sites.append((i + 1, length))
    return sites

fasta = """
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""

sequences = parse_fasta(fasta)
dna = next(iter(sequences.values()))

for position, length in find_reverse_palindromes(dna):
    print(position, length)
