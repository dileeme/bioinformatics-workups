def dna_complement(dna):
    complement_map = {'A': 'T', 'T': 'A', 'C':'G','G':'C'} 
    complement = ''.join(complement_map[base] for base in dna) 
    return complement

dna_sequence = "ATTTAGGCTAGCTTAGGCTTATTTCGGGATATATGCGATTTCGATCTTATTCGAGGGAT" 
print(dna_complement(dna_sequence))

def dna_translate(dna):
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
        "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W"
    } 

    protein = ""
    for i in range(0,len(dna) - len(dna)%3, 3):
        codon = dna[i:i+3]
        protein += codon_table.get(codon, "?")

    return protein

dna_sequence = "ATACTCGGATTCGATTCTATATCGTTATGATGAUUGTUGATGTGGTCTTCT" 
print(dna_translate(dna_sequence))
