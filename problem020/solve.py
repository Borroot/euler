from functools import reduce

fact = reduce(lambda x, y: x * y, list(range(1, 101)))
print(sum([int(i) for i in str(fact)]))
