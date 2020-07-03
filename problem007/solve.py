primes = [2, 3]
last = 3

def prime(x):
    for prime in primes:
        if x % prime == 0:
            return False
    return True

while len(primes) != 10001:
    last += 2
    if prime(last):
        primes.append(last)

print(primes[len(primes) - 1])
