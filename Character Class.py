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


class Enemy(Characters):
    def __init__(self, name, description, health, room, item_drop):
        self.room = room
        self.item = item_drop
        super(Enemy, self). __init__(name, description, health)

    def attack(self, damage):
        print("%s attacked you")


user = User('Player', 'You are an average person not knowing a lot about what is around him.', 100, 10, None)
enemy = Enemy('Zombie', 'One of many zombies', 85, ['pond', 'street', 'street2', 'street3', 'street4', 'park',
                                                    'playground', 's_gated_area', 'w_gated_area'], 'food')
