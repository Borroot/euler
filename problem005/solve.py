found = False
x = 0

while not found:
    x += 20
    for i in range(1, 21):
        if x % i != 0:
            break
        elif i == 20:
            found = True

print(x)
