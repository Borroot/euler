import math

size = 1000000
numbers = [True] * (size - 2)

for i in range(2, math.floor(math.sqrt(size)) + 1):
    if numbers[i - 2]:
        for j in range(i**2, size, i):
            numbers[j - 2] = False

primes = [i + 2 for i, x in enumerate(numbers) if x]
primesset = set(primes[:len(primes) - 1])

upper = 0
index = 0
while upper < 1000000:
    upper += primes[index]
    index += 1

upperindex = index - 1

for window in range(upperindex, 1, -1):
    print(window)
    total = sum(primes[:window + 1])
    offset = 1

    if total in primesset:
        exit()

    while offset + window < len(primes):
        total += primes[window + offset] - primes[offset - 1]

        if total in primesset:
            print(total)
            exit()

        offset += 1
