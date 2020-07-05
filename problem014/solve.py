counts = [1] * 1000000

def new(n):
    return int(n / 2) if n % 2 == 0 else 3*n + 1

for i in range(1, 1000000):
    n = i
    while (n := new(n)) != 1:
        counts[i] += 1
        if n < i:
            counts[i] += counts[n]
            break

print(counts.index(max(counts)))
