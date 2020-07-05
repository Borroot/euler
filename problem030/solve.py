print(sum([x for x in range(2, 1000000) if x == sum([int(digit)**5 for digit in str(x)])]))
