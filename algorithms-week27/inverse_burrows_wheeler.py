def inverse_burrows_wheeler(bwt):
    n = len(bwt)
    table = [""] * n
    for _ in range(n):
        table = sorted(bwt[i] + table[i] for i in range(n))
    for row in table:
        if row.endswith("$"):
            return row

bwt = "annb$aa"

print(inverse_burrows_wheeler(bwt))
