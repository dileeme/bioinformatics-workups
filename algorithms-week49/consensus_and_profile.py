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

def build_profile(dna_strings):
    length = len(dna_strings[0])
    profile = {base: [0] * length for base in "ACGT"}
    for dna in dna_strings:
        for i, base in enumerate(dna):
            profile[base][i] += 1
    return profile

def consensus(profile, length):
    bases = "ACGT"
    return "".join(max(bases, key=lambda base: profile[base][i]) for i in range(length))

fasta = """
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

sequences = list(parse_fasta(fasta).values())
profile = build_profile(sequences)

print(consensus(profile, len(sequences[0])))
for base in "ACGT":
    print(f"{base}: {' '.join(str(count) for count in profile[base])}")
