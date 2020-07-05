def d(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total

total = 0
for a in range(1, 10000):
    b = d(a)
    if a < b and d(b) == a:
        total += a + b

print(total)
