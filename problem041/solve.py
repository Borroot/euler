from itertools import permutations
import math

size = 100000000
numbers = [True] * (size - 2)

for i in range(2, math.floor(math.sqrt(size)) + 1):
    print(i)
    if numbers[i - 2]:
        for j in range(i**2, size, i):
            numbers[j - 2] = False

primes = [i + 2 for i, x in enumerate(numbers) if x]

for n in range(8, 1, -1):
    perms = list(permutations(list(range(1, n))))
    for perm in perms[::-1]:
        pandigit = int(''.join(map(str, perm)))
        if pandigit in primes:
            print(pandigit)
            exit()
