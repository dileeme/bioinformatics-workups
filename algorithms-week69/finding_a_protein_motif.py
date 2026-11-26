def has_n_glycosylation_motif(seq, i):
    if seq[i] != "N":
        return False
    if seq[i + 1] == "P":
        return False
    if seq[i + 2] not in ("S", "T"):
        return False
    if seq[i + 3] == "P":
        return False
    return True

def find_motif_positions(seq):
    return [i + 1 for i in range(len(seq) - 3) if has_n_glycosylation_motif(seq, i)]

proteins = {
    "TEST_P12345": "MVNLTKSPQRSTVNDTAGGNASVPNPTSWERTYNSTPKL",
    "TEST_Q67890": "AGPEPTIDENATPSEQNATSGVLMKPNVTSFFF",
    "TEST_R11223": "MKPEPTIDESEQUENCEWITHOUTMOTIFHERE",
}

for protein_id, seq in proteins.items():
    positions = find_motif_positions(seq)
    if positions:
        print(protein_id)
        print(" ".join(str(p) for p in positions))
