# Defining a class
class Cheeseburger(object):
    def __init__(self, patty_type, cheese):  # TWO underscores before and after
        self.patty = patty_type
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("You cut the cheeseburger")

    def eat(self):
        print("You eat the cheeseburger")
        self.eaten = True


# Instantiating (The creation of) two cheeseburgers
burger1 = Cheeseburger("Beef", "American")
burger2 = Cheeseburger("Bacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)
