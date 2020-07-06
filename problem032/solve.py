from itertools import permutations
import math

perms = list(permutations(list(range(1, 10))))

pandigital = []
for perm in perms:
    for i in range(1, 8):
        for j in range(i + 1, 9):
            a = int(''.join(map(str, perm[:i])))
            b = int(''.join(map(str, perm[i:j])))
            c = int(''.join(map(str, perm[j:])))
            if a < b and a * b == c:
                pandigital.append(c)
                print(f'{a} x {b} = {c}')

print(sum(set(pandigital)))
