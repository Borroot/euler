from math import factorial

print(sum(i for i in range(3, 100000) if sum([factorial(int(x)) for x in str(i)]) == i))
