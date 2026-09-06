def reconstruct_from_path(kmers):
    genome = kmers[0]
    for kmer in kmers[1:]:
        genome += kmer[-1]
    return genome

kmers = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]

print(reconstruct_from_path(kmers))
