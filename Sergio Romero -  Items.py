class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage_dealt):
        self.damage_dealt = damage_dealt
        super(Weapon, self). __init__(name, description)

class Consumable(Item):
    def __init__(self, name, description, hunger_restored):
        self.hunger_restored = hunger_restored
        super(Consumable, self). __init__(name, description)
