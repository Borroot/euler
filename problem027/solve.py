import math

def isprime(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 2:
        return True

    for i in range(3, math.floor(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True

maximum = 0
product = 0
for a in range(-999, 1000):
    print(a)
    for b in range(1, 1001, 2):
        n = 0
        while isprime(n**2 + a*n + b):
            n += 1

        if n > maximum:
            maximum = n
            product = a * b

print(product)
