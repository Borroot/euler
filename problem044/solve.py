pentagonals = [(n * (3*n - 1)) // 2 for n in range(1, 100000)]
pentagonalsset = set(pentagonals)

for p1 in pentagonals:
    print(p1)
    for p2 in pentagonals[pentagonals.index(p1) + 1:]:
        if p1 + p2 in pentagonalsset and p2 - p1 in pentagonalsset:
            print(p2 - p1)
            exit()
