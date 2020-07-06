cycles = []

for d in range(1, 1001):
    count = 0
    seen = []
    remainder = 10

    while (remainder := (remainder % d) * 10) != 0:
        if remainder in seen:
            break
        else:
            count += 1
            seen.append(remainder)

    if remainder == 0:
        count = 0

    cycles.append(count)

print(cycles.index(max(cycles)) + 1)
