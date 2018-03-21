health = 200
hunger = 150
thirst = 100


class Item(object):
    def __init__(self, name, description, is_picked, room, used):
        self.name = name
        self.description = description
        self.is_picked = is_picked
        self.room = room
        self.used = used


class Weapons(Item):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.damage_dealt = damage_dealt
        super(Weapons, self). __init__(name, description, is_picked, room, used)

    def attack(self):
        print("You attack with %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Consumable(Item):
    def __init__(self, name, description, hunger_restored, is_picked, room, used):
        self.hunger_restored = hunger_restored
        super(Consumable, self). __init__(name, description, is_picked, room, used)

    def eat(self):
        print("You ate %s" % self.name)


class Wearable(Item):
    def __init__(self, name, description, storage, is_picked, room, used):
        self.storage = storage
        super(Wearable, self). __init__(name, description, is_picked, room, used)

    def wear(self):
        print("You put on %s" % self.name)


class KeyToPond(Item):
    def __init__(self, name, description, is_picked, room, used):
        super(KeyToPond, self). __init__(name, description, is_picked, room, used)

    def drop(self):
        print("You dropped %s" % self.name)

class Ranged(Weapons):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Ranged, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Melee(Weapons):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Melee, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        print("You attack with %s" % self.name)


class Crossbow(Ranged):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Crossbow, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Guns(Ranged):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Guns, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)


class Shotgun(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Shotgun, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)


class AssaultRifle(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(AssaultRifle, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)


class SemiAutoSniper(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(SemiAutoSniper, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)


class Axe(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Axe, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        print("You attack with %s" % self.name)

class Knife(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Knife, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        print("You attack with ")

class Backpack(Wearable):
    def __init__(self, name, description, storage, is_picked, room, used):
        super(Backpack, self). __init__(name, description, storage, is_picked, room, used)

    def wear(self):
        print("You put on %s" % self.name)


class Food(Consumable):
    def __init__(self, name, description, hunger_restored, is_picked, room, used):
        super(Food, self). __init__(name, description, hunger_restored, is_picked, room, used)

    def eat(self):
        print("You ate %s and restored 25 hunger points." % self.name)


class Healing(Consumable):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(Healing, self). __init__(name, description, health_restored, is_picked, room, used)


class Bandages(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(Bandages, self). __init__(name, description, health_restored, is_picked, room, used)


class HealingPotion(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(HealingPotion, self). __init__(name, description, health_restored, is_picked, room, used)
