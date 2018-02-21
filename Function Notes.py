# Defining functions
def hello_world():
    print("Hello World")


hello_world()


def square_it(number):
    return number**2


print(square_it(3))


def tip_calc(num):
    return num + num * 0.18


print("Your bill is $%d" % tip_calc(100))


def distance_calc(x1, y1, x2, y2):
#       return (x2 - x1) ** 2 + (y2 - y1) ** 2
        inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
        answer = inside ** 0.5
        return answer


def pt_calc(a, b):
    return (a**2 + b**2) ** 0.5


print(pt_calc(3, 6))
print(distance_calc(0, 0, 3, 4))
