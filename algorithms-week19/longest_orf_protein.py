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
    "TAC":"Y", "TAT":"Y", "TAA":"Stop", "TAG":"Stop",
    "TGC":"C", "TGT":"C", "TGA":"Stop", "TGG":"W",
}

def reverse_complement(dna):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(dna))

def find_orf_proteins(strand):
    proteins = []
    for frame in range(3):
        i = frame
        while i + 3 <= len(strand):
            if strand[i:i + 3] == "ATG":
                protein = ""
                j = i
                while j + 3 <= len(strand):
                    amino_acid = codon_table[strand[j:j + 3]]
                    if amino_acid == "Stop":
                        proteins.append(protein)
                        break
                    protein += amino_acid
                    j += 3
            i += 3
    return proteins

def longest_orf_protein(dna):
    candidates = find_orf_proteins(dna) + find_orf_proteins(reverse_complement(dna))
    return max(candidates, key=len)

dna = "GCGATGCTGGGGCCGCGGTCGTAAGCGGCGGCG"

print(longest_orf_protein(dna))
