solutions = [0] * 1000

for p in range(3, 1001):
    print(p)
    for c in range(1, p - 2):
        for b in range(1, p - 1 - c):
            a = p - b - c
            if a <= b and a**2 + b**2 == c**2:
                solutions[p - 1] += 1

print(solutions.index(max(solutions)) + 1)
