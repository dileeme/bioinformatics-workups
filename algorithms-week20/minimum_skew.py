def minimum_skew_positions(genome):
    skew = 0
    min_skew = 0
    positions = [0]
    for i, base in enumerate(genome, start=1):
        if base == "G":
            skew += 1
        elif base == "C":
            skew -= 1
        if skew < min_skew:
            min_skew = skew
            positions = [i]
        elif skew == min_skew:
            positions.append(i)
    return positions

genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

print(" ".join(str(p) for p in minimum_skew_positions(genome)))
