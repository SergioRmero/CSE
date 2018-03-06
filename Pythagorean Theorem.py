def df(x1, y1, x2, y2):
    return((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def pythagorean(a, b):
    return (a ** 2 + b ** 2) ** 0.5


print(pythagorean(5, 3))
print(df(0, 0, 3, 4))
