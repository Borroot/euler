a = 1
b = 1
count = 2

while len(str(a)) < 1000:
    tmp = a
    a = a + b
    b = tmp
    count += 1

print(count)
