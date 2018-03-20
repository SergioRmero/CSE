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


class KeyToPond(Item):
    def __init__(self, name, description, is_picked, room, used):
        super(KeyToPond, self). __init__(name, description, is_picked, room, used)


class Ranged(Weapons):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Ranged, self). __init__(name, description, damage_dealt, is_picked, room, used)


class Melee(Weapons):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Melee, self). __init__(name, description, damage_dealt, is_picked, room, used)


class Crossbow(Ranged):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Crossbow, self). __init__(name, description, damage_dealt, is_picked, room, used)


class Guns(Ranged):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Guns, self). __init__(name, description, damage_dealt, is_picked, room, used)


class Shotgun(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Shotgun, self). __init__(name, description, damage_dealt, is_picked, room, used)


class AssaultRifle(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(AssaultRifle, self). __init__(name, description, damage_dealt, is_picked, room, used)


class SemiAutoSniper(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(SemiAutoSniper, self). __init__(name, description, damage_dealt, is_picked, room, used)


class Axe(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Axe, self). __init__(name, description, damage_dealt, is_picked, room, used)


class Knife(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Knife, self). __init__(name, description, damage_dealt, is_picked, room, used)


class Backpack(Wearable):
    def __init__(self, name, description, storage, is_picked, room, used):
        super(Backpack, self). __init__(name, description, storage, is_picked, room, used)


class Food(Consumable):
    def __init__(self, name, description, hunger_restored, is_picked, room, used):
        super(Food, self). __init__(name, description, hunger_restored, is_picked, room, used)


class Healing(Consumable):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(Healing, self). __init__(name, description, health_restored, is_picked, room, used)


class Bandages(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(Bandages, self). __init__(name, description, health_restored, is_picked, room, used)


class HealingPotion(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(HealingPotion, self). __init__(name, description, health_restored, is_picked, room, used)
