# 12.4.17
def reverse_order(first_name, last_name):
    print ("%s, %s" % (last_name, first_name))
    # or print (last_name + " " + first_name


reverse_order("Sergio", "Romero")


# 12.5.17
def add_py(name):
    print("%s.py" % name)
    # or print(name + .py)


add_py("Sergio") == "Sergio.py"


# 12.6.17
def add(num1, num2, num3): # can call parameters whatever you want
    print(num1 + num2 + num3)


add(15, 18, 9000)
add(60, 90, 100)


# 12.7.17
for x in range(3):
    print("Hello")

