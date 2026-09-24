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

def longest_shared_motif(sequences, min_length=20):
    shortest = min(sequences, key=len)
    for length in range(len(shortest), min_length - 1, -1):
        for start in range(len(shortest) - length + 1):
            candidate = shortest[start:start + length]
            if all(candidate in seq for seq in sequences):
                return candidate
    return ""

fasta = """
>Rosalind_1
EIWCWWPCIMFPCDVENWCTHCDQQDIDVQCVFLQF
>Rosalind_2
EWLVGEWWHMFPCDVENWCTHCDQQDIDVQCEVDWCYH
>Rosalind_3
VQMRWRNLMFPCDVENWCTHCDQQDIDVQCGIDWLT
>Rosalind_4
MRLYDETQMFPCDVENWCTHCDQQDIDVQCMFSQCD
"""

sequences = list(parse_fasta(fasta).values())
motif = longest_shared_motif(sequences)

print(motif)
