coins = [1, 2, 5, 10, 20, 50, 100, 200]

def pay(goal, current, last):
    if current > goal:
        return 0
    if current == goal:
        return 1

    total = 0
    for coin in coins[coins.index(last):]:
        total += pay(goal, current + coin, coin)
    return total

print(pay(200, 0, 1))
