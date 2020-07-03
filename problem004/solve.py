p = 0

for x in range(900, 1000):
    for y in range(900, 1000):
        tmp = str(x * y)
        if tmp == tmp[::-1] and int(tmp) > p:
            p = int(tmp)

print(p)
