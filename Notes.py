# print("Hello World")
#
# # Sergio Romero, comment
#
# a = 4
# b = 3
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print()
# print("Try to figure out how this works")
# print(13 % 12)
#
# # the "%" sign is a modulus. It finds the remainder
#
# car_name = "The Wiebe Mobile"
# car_type = "BMW"
# car_cylinders = 8
# car_mpg = 5000.9
#
# print("I have a car called %s. It's pretty nice" % car_name)
# print("I have a car called %s. It's a %s" % (car_name, car_type)) # watch the order
#
# Here is where we get a little fancy
# print("What is your name?")
# name = input(">_ ")
# print("Hello %s." % name)
#
# age = input("How old are you?")
# print("%s?!  That's really old. You belong in a retirement home." % age)
#
# print("I'm adding some code")
# indent is exactly 4 spaces in python
# Functions


def print_hw():
    print_hw("Hello World.")
    print_hw("Enjoy the day.")


def say_hi(name): # name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("Sergio")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age = age + 1 # or age += 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("Sergio", 14)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7*x - 4

print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80 : # elif = else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print (grade_calc(64))
