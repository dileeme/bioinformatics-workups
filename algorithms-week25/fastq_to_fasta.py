def parse_fastq(text):
    lines = text.strip().splitlines()
    records = []
    for i in range(0, len(lines), 4):
        header = lines[i][1:].strip()
        seq = lines[i + 1].strip()
        records.append((header, seq))
    return records

fastq = """
@Rosalind_0040
GCCCCAGGCTGCATGCCCACCTGGCTAGACGCTATATCGCC
+
6.699958..99.599999977899.9999999998899999
@Rosalind_0041
TCGTATGCGTAGCACTGGGCATGATGGGCGGCGCGTATCGT
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
"""

for header, seq in parse_fastq(fastq):
    print(f">{header}")
    print(seq)
