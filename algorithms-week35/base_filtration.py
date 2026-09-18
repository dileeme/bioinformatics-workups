def parse_fastq(text):
    lines = text.strip().splitlines()
    records = []
    for i in range(0, len(lines), 4):
        label = lines[i][1:].strip()
        seq = lines[i + 1].strip()
        qual = lines[i + 3].strip()
        records.append((label, seq, qual))
    return records

def trim_read(seq, qual, threshold):
    quals = [ord(ch) - 33 for ch in qual]
    start = 0
    while start < len(quals) and quals[start] < threshold:
        start += 1
    end = len(quals)
    while end > start and quals[end - 1] < threshold:
        end -= 1
    return seq[start:end]

threshold_quality = 20

fastq = """
@Rosalind_0031_1
ACGTACGT
+
!!IIIIII
@Rosalind_0031_2
TTAGGCCA
+
IIIIII!!
@Rosalind_0031_3
CCGGTTAA
+
!IIIIII!
"""

records = parse_fastq(fastq)

for label, seq, qual in records:
    print(">" + label)
    print(trim_read(seq, qual, threshold_quality))
