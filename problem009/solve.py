for c in range(997, 333, -1):
    for b in range(min(999 - c, c - 1), (999 - c) // 2 + 1, -1):
        a = 1000 - b - c
        if a**2 + b**2 == c**2:
            print(a * b * c)
