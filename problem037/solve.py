primes = [2]
last = 3

def isprime(n):
    for prime in primes:
        if n % prime == 0:
            return False
        if prime > n // 2:
            return True
    return True

while primes[len(primes) - 1] < 1000000:
    if isprime(last):
        primes.append(last)
        print(last)
    last += 2

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
