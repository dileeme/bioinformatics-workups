standard_table = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

mito_table = dict(standard_table)
mito_table["AGA"] = "*"
mito_table["AGG"] = "*"
mito_table["ATA"] = "M"
mito_table["TGA"] = "W"

genetic_codes = {1: standard_table, 2: mito_table}

def translate(dna, table):
    protein = ""
    for i in range(0, len(dna) - 2, 3):
        amino_acid = table[dna[i:i + 3]]
        if amino_acid == "*":
            break
        protein += amino_acid
    return protein

def find_genetic_code(dna, protein):
    for index, table in genetic_codes.items():
        if translate(dna, table) == protein:
            return index
    return None

dna = "ATGTGGTGA"
protein = "MWW"

print(find_genetic_code(dna, protein))
