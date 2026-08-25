from collections import Counter

def parse_fasta(text):
    sequences = []
    label = None
    for line in text.strip().splitlines():
        if line.startswith(">"):
            label = line[1:].strip()
            sequences.append("")
        else:
            sequences[-1] += line.strip()
    return sequences

def reverse_complement(s):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[b] for b in reversed(s))

def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

def correct_reads(reads):
    counts = Counter(reads)
    correct = set()
    for read in counts:
        if counts[read] + counts[reverse_complement(read)] > 1:
            correct.add(read)

    corrections = []
    for read in reads:
        if read in correct:
            continue
        for candidate in correct:
            if hamming_distance(read, candidate) == 1:
                corrections.append((read, candidate))
                break
            rc_candidate = reverse_complement(candidate)
            if hamming_distance(read, rc_candidate) == 1:
                corrections.append((read, rc_candidate))
                break
    return corrections

fasta = """
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC
>Rosalind_30
TGAAA
"""

reads = parse_fasta(fasta)

for original, fixed in correct_reads(reads):
    print(f"{original}->{fixed}")
