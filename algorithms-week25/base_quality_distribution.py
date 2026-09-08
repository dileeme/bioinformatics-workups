def parse_fastq(text):
    lines = text.strip().splitlines()
    records = []
    for i in range(0, len(lines), 4):
        seq = lines[i + 1].strip()
        qual = lines[i + 3].strip()
        records.append((seq, qual))
    return records

def first_position_below_threshold(records, threshold):
    quals = [qual for seq, qual in records]
    length = len(quals[0])
    for pos in range(length):
        mean_quality = sum(ord(qual[pos]) - 33 for qual in quals) / len(quals)
        if mean_quality < threshold:
            return pos + 1
    return -1

threshold_quality = 20

fastq = """
@Rosalind_0070_1
GATTACAGATTACA
+
IIIII+IIIIIIII
@Rosalind_0070_2
GATTACAGATTACA
+
IIIII+IIIIIIII
@Rosalind_0070_3
GATTACAGATTACA
+
IIIII+IIIIIIII
"""

records = parse_fastq(fastq)
print(first_position_below_threshold(records, threshold_quality))
