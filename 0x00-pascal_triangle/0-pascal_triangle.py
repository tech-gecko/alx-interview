import math

def pascal_triangle(n):
    triangle = []

    if n <= 0:
        return triangle

    else:
        for row in range(n):
            triangle.append([math.comb(row, index) for index in range(row + 1)])

    return triangle