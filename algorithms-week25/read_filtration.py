def parse_fastq(text):
    lines = text.strip().splitlines()
    records = []
    for i in range(0, len(lines), 4):
        seq = lines[i + 1].strip()
        qual = lines[i + 3].strip()
        records.append((seq, qual))
    return records

def passes_quality_filter(qual, threshold, percentage):
    good_bases = sum(1 for ch in qual if ord(ch) - 33 >= threshold)
    return (good_bases / len(qual)) * 100 >= percentage

def count_passing_reads(records, threshold, percentage):
    return sum(1 for seq, qual in records if passes_quality_filter(qual, threshold, percentage))

threshold_quality = 20
threshold_percentage = 50

fastq = """
@Rosalind_0060_1
GATTACAGAT
+
IIIIIIIIII
@Rosalind_0060_2
GATTACAGAT
+
!!!!!!!!!!
@Rosalind_0060_3
GATTACAGAT
+
IIIII!!!!!
@Rosalind_0060_4
GATTACAGAT
+
IIIIIIII!!
"""

records = parse_fastq(fastq)
print(count_passing_reads(records, threshold_quality, threshold_percentage))
