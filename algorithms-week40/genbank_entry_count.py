def count_genbank_entries(records, genus, start_date, end_date):
    count = 0
    for organism, pub_date in records:
        if organism.split()[0] == genus and start_date <= pub_date <= end_date:
            count += 1
    return count

records = [
    ("Anthoxanthum aristatum", "2003-05-14"),
    ("Anthoxanthum aristatum", "2003-07-25"),
    ("Anthoxanthum nipponicum", "2004-02-10"),
    ("Anthoxanthum odoratum", "2005-01-15"),
    ("Anthoxanthum ovatum", "2005-12-27"),
    ("Anthoxanthum rupestre", "2006-03-02"),
    ("Chlamydomonas reinhardtii", "2004-06-01"),
]

genus = "Anthoxanthum"
start_date = "2003-07-25"
end_date = "2005-12-27"

print(count_genbank_entries(records, genus, start_date, end_date))
