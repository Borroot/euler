import math

triangle = 1
number = 2

found = False
while not found:
    triangle += number
    number += 1

    count = 2
    for divisor in range(2, math.floor(math.sqrt(triangle))):
        if triangle % divisor == 0:
            count += 2  # because of mirror factors!

    print(f'{triangle:<12} {count:<5}')
    if count >= 500:
        found = True
        print(triangle)
