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
# ar_type = "BMW"
# car_cylinders = 8
# car_mpg = 5000.9

# print("I have a car called %s. It's pretty nice" % car_name)
# print("I have a car called %s. It's a %s" % (car_name, car_type)) # watch the order

# Here is where we get a little fancy
# print("What is your name?")
# name = input(">_ ")
# print("Hello %s." % name)

# age = input("How old are you?")
# print("%s?!  That's really old. You belong in a retirement home." % age)

# print("I'm adding some code")
# indent is exactly 4 spaces in python
# Functions


# def print_hw():
# print_hw("Hello World.")
# print_hw("Enjoy the day.")


# def say_hi(name): # name is a "parameter"
# print("Hello %s" % name)
# print("Coding is great!")


# say_hi("Sergio")


# def print_age(name, age):
# #   print("%s is %d years old" % (name, age))
#  #  age = age + 1 # or age += 1
#   # print("Next year, %s will be %d years old" % (name, age))


# print_age("Sergio", 14)


# def algebra_hw(x):
#   return x**3 + 4*x**2 + 7*x - 4

# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))


# if statements


# def grade_calc(percentage):
#    if percentage >= 90:
#        return "A"
#    elif percentage >= 80 : # elif = else if
#        return "B"
#    elif percentage >= 70:
#     #   return "C"
#    #elif percentage >= 60:
#     #   return "D"
#    else:
#    return "F"


# print (grade_calc(79.9))


# def happy_b_day(name):
#   print("Happy Birthday to you, Happy Birthday to you Happy Birthday dear %s, Happy Birthday to you!" % name)


# happy_bday("computer")

# Loops

# for num in range(10):
#  print(num + 1)

# While loops (BEWARE!!!!!)

# a = 1
# while a < 10: # This is the condition, it must be true to execute
#    print(a)
#    a += 1  # This iterates so that we can break the loop


# Random Numbers
# import random  # This should be on line 1
# print(random.randint(0,1000))


# Recasting
# c = '1'
# print(c == 1) # we have a string and an integer
# print(int(c) ==1 )
# print(c == str(1))


# Comparisons

# print(1 == 1) # Use a double equal sign
# print(1 != 2) # 1 is not equal to 2
# print(not False) # "!" is the "not" operator

# Lists

the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', 'beef', 'sauce', 'sesame seed bun', 'avocado', 'onion']
# print(cheeseburger_ingredients[0])
# print(cheeseburger_ingredients[3])
# print(len(cheeseburger_ingredients))
# print(len(the_count))

# Going through lists

for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for num in the_count:
    print(num * 2)

length = len(cheeseburger_ingredients)
range(5)  # A list of the numbers 0 through 4
range(len(cheeseburger_ingredients))  # Generates a list of all indices

for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s" % (num, item))

