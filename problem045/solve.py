triangles = [(n * (  n + 1)) // 2 for n in range(1, 100000)]
pentagons = {(n * (3*n - 1)) // 2 for n in range(1, 1000000)}
hexagons  = { n * (2*n - 1)       for n in range(1, 1000000)}

for index, triangle in enumerate(triangles):
    print(index)
    if index > 284 and triangle in pentagons and triangle in hexagons:
        print(triangle)
        break
