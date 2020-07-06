size = 1001
grid = [[0] * size for _ in range(0, size)]

grid[size // 2][size // 2] = 1

last = 1
step = 3
y, x = (size // 2, size // 2 + 1)

for _ in range(0, size // 2):
    for i in range(1, step):
        grid[y + i - 1][x] = (last := last + 1)
    for i in range(1, step):
        grid[y + step - 2][x - i] = (last := last + 1)
    for i in range(1, step):
        grid[y + step - 2 - i][x - step + 1] = (last := last + 1)
    for i in range(1, step):
        grid[y - 1][x - step + 1 + i] = (last := last + 1)

    step += 2
    x += 1
    y -= 1

total = 0
for i in range(0, size):
    total += grid[i][i]
    total += grid[i][size - 1 - i]

print(total - 1)
