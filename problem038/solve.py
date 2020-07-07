def ispandigital(n):
    if len(n) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True

largest = -1
for n in range(1, 50000):
    concat = ''
    mult = 1
    while len(concat) < 9:
        concat += str(n * mult)
        mult += 1

    if ispandigital(concat) and largest < int(concat):
        largest = int(concat)

print(largest)
