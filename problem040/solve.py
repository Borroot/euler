last = 1
fraction = ""
while len(fraction) < 1000000:
    fraction += str(last)
    last += 1

product = 1
current = 1
while current <= 1000000:
    product *= int(fraction[current - 1])
    current *= 10

print(product)
