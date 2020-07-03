primes = [2, 3]
last = 3

def prime(x):
    for prime in primes:
        if x % prime == 0:
            return False
    return True

while primes[len(primes) - 1] < 2000000:
    last += 2
    if prime(last):
        primes.append(last)
        print(last)

print(sum(primes) - primes[len(primes) - 1])
