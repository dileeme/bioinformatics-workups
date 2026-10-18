def count_entries_in_range(entries, genus, start, end):
    count = 0
    for entry_genus, published in entries:
        if entry_genus == genus and start <= published <= end:
            count += 1
    return count

entries = [
    ("Anthoxanthum", (2003, 7, 25)),
    ("Anthoxanthum", (2004, 1, 15)),
    ("Anthoxanthum", (2005, 12, 27)),
    ("Anthoxanthum", (2006, 3, 10)),
    ("Zea", (2004, 5, 1)),
    ("Anthoxanthum", (2003, 2, 2)),
]

genus = "Anthoxanthum"
start = (2003, 7, 25)
end = (2005, 12, 27)

print(count_entries_in_range(entries, genus, start, end))
