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
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna, min_len=4, max_len=12):
    sites = []
    for length in range(min_len, max_len + 1, 2):
        for start in range(len(dna) - length + 1):
            substring = dna[start:start + length]
            if substring == reverse_complement(substring):
                sites.append((start + 1, length))
    return sites

fasta = """
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""

sequences = parse_fasta(fasta)
dna = list(sequences.values())[0]

for position, length in find_reverse_palindromes(dna):
    print(position, length)
