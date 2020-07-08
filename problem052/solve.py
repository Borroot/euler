def permutation(a, b):
    return sorted(list(str(a))) == sorted(list(str(b)))

def teller(n):
    for i in range(2, 7):
        if not permutation(n, i * n):
            return False
    return True

for n in range(1, 1000000):
    if teller(n):
        print(n)
        break
