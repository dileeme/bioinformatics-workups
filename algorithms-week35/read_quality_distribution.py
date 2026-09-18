def parse_fastq(text):
    lines = text.strip().splitlines()
    records = []
    for i in range(0, len(lines), 4):
        seq = lines[i + 1].strip()
        qual = lines[i + 3].strip()
        records.append((seq, qual))
    return records

def mean_quality(qual):
    return sum(ord(ch) - 33 for ch in qual) / len(qual)

def count_below_threshold(records, threshold):
    return sum(1 for seq, qual in records if mean_quality(qual) < threshold)

threshold_quality = 26

fastq = """
@Rosalind_0041_1
GATTACA
+
GGGGGGG
@Rosalind_0041_2
GATTACA
+
!!!!!!!
@Rosalind_0041_3
GATTA
+
III!!
"""

records = parse_fastq(fastq)

print(count_below_threshold(records, threshold_quality))
