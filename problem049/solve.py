import math

size = 10000
numbers = [True] * (size - 2)

for i in range(2, math.floor(math.sqrt(size)) + 1):
    if numbers[i - 2]:
        for j in range(i**2, size, i):
            numbers[j - 2] = False

primes = [i + 2 for i, x in enumerate(numbers) if x and len(str(i + 2)) == 4]
primesset = set(primes)

def perm(a, b):
    return sorted(list(str(a))) == sorted(list(str(b)))

for prime in primes:
    for add in range(2, (10000 - prime) // 2, 2):
        found = True

        for i in range(1, 3):
            new = prime + add * i
            if not perm(prime, new) or new not in primes:
                found = False
                break

        if found:
            print(prime, prime + add, prime + add * 2, sep='')
