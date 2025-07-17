def load_dna_sequence(file_path):
    with open(file_path, 'r') as f:
        return f.read().replace("\n", "").upper()

def search_subsequence(dna_seq, query):
    query = query.upper()
    positions = []
    for i in range(len(dna_seq) - len(query) + 1):
        if dna_seq[i:i+len(query)] == query:
            positions.append(i)
    return positions

def main():
    file_path = "sample_dna.txt"
    dna_seq = load_dna_sequence(file_path)

    print(f"Loaded DNA sequence of length {len(dna_seq)}")
    query = input("Enter the DNA subsequence to search: ").strip().upper()

    matches = search_subsequence(dna_seq, query)

    if matches:
        print(f"\nFound {len(matches)} matches at positions:")
        print(matches)
    else:
        print("\nNo matches found.")

if __name__ == "__main__":
    main()
