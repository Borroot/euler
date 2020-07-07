import math

size = 250000
numbers = [True] * (size - 2)

for i in range(2, math.floor(math.sqrt(size)) + 1):
    if numbers[i - 2]:
        for j in range(i**2, size, i):
            numbers[j - 2] = False

primes = [i + 2 for i, x in enumerate(numbers) if x]
primesset = set(primes)

def factorize(n):
    factors = []
    index = 0
    while n != 1:
        if n % primes[index] == 0:
            n //= primes[index]
            factors.append(primes[index])
        else:
            index += 1
    return len(set(factors))

teller = 0
for n in range(1, size):
    print(n)
    if n not in primesset and factorize(n) == 4:
        teller += 1
        if teller == 4:
            print(n - 3)
            break
    else:
        teller = 0
