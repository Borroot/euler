from itertools import permutations

print(''.join(map(str, list(permutations(list(range(0, 10))))[999999])))
