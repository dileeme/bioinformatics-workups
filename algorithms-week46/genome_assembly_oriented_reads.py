def reverse_complement(seq):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(seq))

def assemble_from_oriented_reads(reads):
    k = len(reads[0])
    oriented_reads = set()
    for read in reads:
        oriented_reads.add(read)
        oriented_reads.add(reverse_complement(read))

    next_read = {read[:-1]: read for read in oriented_reads}

    genome = reads[0]
    current = reads[0]
    for _ in range(len(reads) - 1):
        current = next_read[current[-(k - 1):]]
        genome += current[-1]

    return genome[:len(reads)]

reads = [
    "CGTCGT", "GTACGT", "CGACGT", "GTGTAC", "ACACGA",
    "TACGTC", "CGTACA", "CGTGTA", "GTCGTG",
]

print(assemble_from_oriented_reads(reads))
