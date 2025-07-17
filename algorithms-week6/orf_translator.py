codon_table = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
    "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W"
}

def translate_dna(dna_seq):
    protein = ""
    for i in range(0, len(dna_seq)-2, 3):
        codon = dna_seq[i:i+3]
        if len(codon) < 3:
            continue
        aa = codon_table.get(codon.upper(), 'X')
        if aa == "*":
            break
        protein += aa
    return protein

def find_orfs(dna_seq):
    orfs = []
    stop_codons = {"TAA", "TAG", "TGA"}
    for frame in range(3):
        i = frame
        while i < len(dna_seq)-2:
            codon = dna_seq[i:i+3]
            if codon == "ATG":
                for j in range(i+3, len(dna_seq)-2, 3):
                    next_codon = dna_seq[j:j+3]
                    if next_codon in stop_codons:
                        orfs.append(dna_seq[i:j+3])
                        break
                i += 3
            else:
                i += 3
    return orfs

def main():
    dna_seq = (
        "AGCTGATGCGTATGACCGTTGAACGTATGCTAGCTAGCGTAAAGCTAGCTGACTAA"
        "ATGGCGTAAATGCGATAGCGGCGATAGTAG"
    )
    
    print("Original DNA sequence:\n", dna_seq)
    print("\nFinding ORFs...\n")

    orfs = find_orfs(dna_seq)

    if not orfs:
        print("No ORFs found.")
        return

    for idx, orf in enumerate(orfs, 1):
        print(f"ORF {idx}:")
        print("DNA:", orf)
        protein = translate_dna(orf)
        print("Protein:", protein)
        print("-" * 40)

if __name__ == "__main__":
    main()
