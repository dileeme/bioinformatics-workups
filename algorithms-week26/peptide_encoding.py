codon_table = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W",
}

def reverse_complement(dna):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(dna))

def translate(dna):
    return "".join(codon_table[dna[i:i + 3]] for i in range(0, len(dna), 3))

def encodes_peptide(substring, peptide):
    return translate(substring) == peptide or translate(reverse_complement(substring)) == peptide

def peptide_encoding_substrings(dna, peptide):
    k = 3 * len(peptide)
    return [dna[i:i + k] for i in range(len(dna) - k + 1) if encodes_peptide(dna[i:i + k], peptide)]

dna = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
peptide = "MA"

for substring in peptide_encoding_substrings(dna, peptide):
    print(substring)
