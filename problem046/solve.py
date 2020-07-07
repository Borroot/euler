import math

size = 10000
numbers = [True] * (size - 2)

for i in range(2, math.floor(math.sqrt(size)) + 1):
    if numbers[i - 2]:
        for j in range(i**2, size, i):
            numbers[j - 2] = False

primes = [i + 2 for i, x in enumerate(numbers) if x]
compos = [i + 2 for i, x in enumerate(numbers) if not x and (i + 2) % 2 == 1]
square = {i**2 for i in range(1, 10000)}

for comp in compos:
    for prime in primes:
        if prime > comp:
            print(comp)
            exit()
        if (comp - prime) // 2 in square:
            break
