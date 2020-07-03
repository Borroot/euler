a = 0
b = 1
fibs = []

while a < 4000000:
    new = a + b
    a = b
    b = new
    fibs.append(b)

print(sum([x for x in fibs if x % 2 == 0]))
