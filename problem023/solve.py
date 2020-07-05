def abundant(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
            if total > n:
                return True
    return False

limit = 28123
abundants = [x for x in list(range(1, limit)) if abundant(x)]

def issum(n):
    print(n)
    for i in range(0, len(abundants)):
        if abundants[i] > n or (abundants[i] % 2 == 0 and n % 2 == 1):
            continue
        for j in range(0, len(abundants)):
            if abundants[i] + abundants[j] == n:
                return True
    return False

print(sum([x for x in list(range(1, limit + 1)) if not issum(x)]))
