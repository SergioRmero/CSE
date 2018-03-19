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
    def __init__(self, name, description, damage_dealt):
        super(Crossbow, self). __init__(name, description, damage_dealt)


class Guns(Ranged):
    def __init__(self, name, description, damage_dealt):
        super(Guns, self). __init__(name, description, damage_dealt)


class Shotgun(Guns):
    def __init__(self, name, description, damage_dealt):
        super(Shotgun, self). __init__(name, description, damage_dealt)


class AssaultRifle(Guns):
    def __init__(self, name, description, damage_dealt):
        super(AssaultRifle, self). __init__(name, description, damage_dealt)


class SemiAutoSniper(Guns):
    def __init__(self, name, description, damage_dealt):
        super(SemiAutoSniper, self). __init__(name, description, damage_dealt)


class Axe(Melee):
    def __init__(self, name, description, damage_dealt):
        super(Axe, self). __init__(name, description, damage_dealt)


class Knife(Melee):
    def __init__(self, name, description, damage_dealt):
        super(Knife, self). __init__(name, description, damage_dealt)


class Backpack(Wearable):
    def __init__(self, name, description, storage):
        super(Backpack, self). __init__(name, description, storage)


class Food(Consumable):
    def __init__(self, name, description, hunger_restored):
        super(Food, self). __init__(name, description, hunger_restored)


class Healing(Consumable):
    def __init__(self, name, description, health_restored):
        super(Healing, self). __init__(name, description, health_restored)


class Bandages(Healing):
    def __init__(self, name, description, health_restored):
        super(Bandages, self). __init__(name, description, health_restored)


class HealingPotion(Healing):
    def __init__(self, name, description, health_restored):
        super(HealingPotion, self). __init__(name, description, health_restored)
