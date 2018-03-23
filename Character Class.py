class Characters(object):
    def __init__(self, name, description, health):
        self.name = name
        self.description = description
        self.health = health


class User(Characters):
    def __init__(self, name, description, health, inventory, position):
        self.space = inventory
        self.pos = position
        super(User, self). __init__(name, description, health)

    def damage(self, amount):
        self.health -= amount
        print("You took %s damage" % self.health)
        
    def take(self, item):
        print("You took %s", item)
