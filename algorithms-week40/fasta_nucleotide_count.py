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

def count_nucleotides(seq):
    return [seq.count(base) for base in "ACGT"]

fasta = """
>Rosalind_7391
GATGGAACTTGACTACGTAAATTCTCCGATCAACGGGATCTCGGCTGCTCCTGATTACG
TATAGTAGAATTACAGGCTTTCGAACTGGATCCGCTACCAGGTAATCGCCGGTAACTCT
GAGTTTAGTGTATATGGGAGTAACTCCTAACATTGAGA
"""

sequences = parse_fasta(fasta)
seq = list(sequences.values())[0]

print(" ".join(str(n) for n in count_nucleotides(seq)))
