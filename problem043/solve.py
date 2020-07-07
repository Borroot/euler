from itertools import permutations

perms = [perm for perm in list(permutations(list(range(0, 10)))) if perm[0] != 0]
divisors = [2, 3, 5, 7, 11, 13, 17]

total = []
for perm in perms:
    correct = True
    for i in range(1, 8):
        number = int(''.join(map(str, perm[i:i + 3])))
        if number % divisors[i - 1] != 0:
            correct = False
            break

    if correct:
        total.append(int(''.join(map(str, perm))))

print(sum(total))
