x = 600851475143
i = 2

while i < x:
    if x % i == 0:
        x //= i
    i += 1

print(x)
