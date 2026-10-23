CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

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

def translate_rna(rna):
    protein = []
    for i in range(0, len(rna), 3):
        amino_acid = CODON_TABLE[rna[i:i + 3]]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    return "".join(protein)

def splice_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, "")
    return dna

fasta = """
>Rosalind_10
ATGGCCATGTTTTTGCGCCCAGAACTGAGATCAATGGGGGAGTACCCGTATTAACGGGTGA
>Rosalind_12
TTTTT
>Rosalind_15
GGGGG
"""

sequences = parse_fasta(fasta)
labels = list(sequences)
dna = sequences[labels[0]]
introns = [sequences[label] for label in labels[1:]]

exon_dna = splice_introns(dna, introns)
rna = exon_dna.replace("T", "U")

print(translate_rna(rna))
