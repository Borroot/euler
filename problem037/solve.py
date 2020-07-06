import math

size = 1000000
numbers = [True] * (size - 2)

for i in range(2, math.floor(math.sqrt(size)) + 1):
    if numbers[i - 2]:
        for j in range(i**2, size, i):
            numbers[j - 2] = False

primes = [i + 2 for i, x in enumerate(numbers) if x]

def istruncatable(prime):
    for i in range(1, len(str(prime))):
        if int(str(prime)[i:]) not in primes or int(str(prime)[:i]) not in primes:
            return False
    return True

truncs = []
for prime in primes:
    if len(str(prime)) > 1 and istruncatable(prime):
        truncs.append(prime)


print(truncs, len(truncs))
print(sum(truncs))
