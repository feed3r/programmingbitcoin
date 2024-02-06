from ecc import Point

points = [(2, 4), (-1, -1), (18,77), (5,7)]

for candidates in points:
    x, y = candidates
    try:
        p = Point(x, y, 5, 7)
        print(f'({x},{y}) is on the curve')
    except ValueError:
        print(f'({x},{y}) is not on the curve')