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
primes.pop()

def iscircular(n):
    print(n)
    for i in range(0, len(str(n))):
        if int(str(n)[i:] + str(n)[:i]) not in primes:
            return False
    return True

print(sum([1 for prime in primes if iscircular(prime)]))
