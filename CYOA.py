health = 200
hunger = 150


class Item(object):
    def __init__(self, name, description, is_picked, room, used):
        self.name = name
        self.description = description
        self.is_picked = is_picked
        self.room = room
        self.used = used

    def drop(self):
        if self.is_picked:
            self.is_picked = False
            print("You drop %s" % self.name)
        else:
            print("You can't drop that.")

    def pick(self):
        if not self.is_picked:
            self.is_picked = True
            print("You picked up %s" % self.name)
        else:
            print("You can't pick that up.")


class Weapons(Item):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.damage_dealt = damage_dealt
        super(Weapons, self). __init__(name, description, is_picked, room, used)

    def attack(self):
        print("You attack with %s" % self.name)


class Consumable(Item):
    def __init__(self, name, description, hunger_restored, is_picked, room, used):
        self.hunger_restored = hunger_restored
        super(Consumable, self). __init__(name, description, is_picked, room, used)

    def use(self):
        print("You used %s" % self.name)


class Wearable(Item):
    def __init__(self, name, description, storage, is_picked, room, used):
        self.storage = storage
        super(Wearable, self). __init__(name, description, is_picked, room, used)

    def wear(self):
        print("You put on %s" % self.name)


class KeyToPond(Item):
    def __init__(self, name, description, is_picked, room, used):
        super(KeyToPond, self). __init__(name, description, is_picked, room, used)

    def use(self):
        print("You used %s to open Gate to Pond" % self.name)


class Ranged(Weapons):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Ranged, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)


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

    def drop(self):
        print("You drop %s" % self.name)


class AssaultRifle(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(AssaultRifle, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class SemiAutoSniper(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(SemiAutoSniper, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self):
        print("You shoot with %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Axe(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Axe, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        print("You attack with %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Knife(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Knife, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        print("You attack with %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Backpack(Wearable):
    def __init__(self, name, description, storage, is_picked, room, used):
        super(Backpack, self). __init__(name, description, storage, is_picked, room, used)

    def wear(self):
        print("You put on %s" % self.name)


class Food(Consumable):
    def __init__(self, name, description, hunger_restored, is_picked, room, used):
        super(Food, self). __init__(name, description, hunger_restored, is_picked, room, used)

    def eat(self):
        self.used = True
        print("You ate %s" % self.name)


class Healing(Consumable):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        self.health = 100
        super(Healing, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self, heal_amount):
        self.health -= heal_amount


class Bandages(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        self.health = 100
        super(Bandages, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self, heal_amount):
        self.health -= heal_amount
        print("You healed 10 hp with %s" % self.name)


class HealingPotion(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        self.health = 100
        super(HealingPotion, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self, heal_amount):
        self.health -= heal_amount
        print("You healed 25 hp with %s" % self.name)


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
        print("You lost %s damage" % self.health)

    def take(self, item):
        print("You took %s", item)


class Enemy(Characters):
    def __init__(self, name, description, health, room, item_drop):
        self.room = room
        self.item = item_drop
        super(Enemy, self). __init__(name, description, health)

    def attack(self, damage):
        self.health -= damage
        print("%s attacked you" % self.name)

    def death(self):
        print('%s has been killed.' % self.name)


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, northeast, southeast, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.northeast = northeast
        self.southeast = southeast
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


Key_To_Pond = Item('Key to Pond', 'This is a key it says pond on the side of it.', False, 'restrooms', False)
crossbow = Crossbow('Crossbow', 'It looks like a crossbow, when it fires the arrow goes very far', 50, False,
                    'secret', False)
shotgun = Shotgun('Shotgun', 'A shotgun, deals the most damage out of all weapons, more sufficient in close range', 70,
                  False, 'secret', False)
assault_rifle = AssaultRifle('Assault Rifle', 'An assault rifle', 35, False, 'secret', False)
semi_auto_snipe = SemiAutoSniper('Semi Auto Sniper', 'A sniper, this does more damage than the'
                                                     ' crossbow', 75, False, 'secret', False)
axe = Axe('Axe', 'An axe, does not do a lot of damage, it looks like it was used to chop wood', 15, False, 'Pond',
          False)
knife = Knife('Knife', 'A knife, does the least damage out of all the weapons', 10, False, 'attic', False)
backpack = Backpack('Backpack', 'A backpack, you could probably put some items in here', 10, False, 'secret', False)
food = Food('Food', 'There is food in a bag, the bag also feels warm.', 25, False, 'restrooms', False)
bandages = Bandages('Bandages', 'Bandages, these heal you when health is low', 30, False, 'rest', False)


# north, south, east, west, up , down, northeast, southeast
spawn = Room("Spawn", 'You are in an empty room with the ceiling light dimly lit.'
             ' There is an open door at the south side of the room',
             None, "west", None, None, None, None, None, None, [])
west = Room("West Room", "There is a door on the east side of the room and a trap door on the floor that seems to be"
            " locked", "spawn", None, "living", None, None, "secret", None, None, [])
secret = Room("Secret Room", "This is a dark room with what seems to"
                             " be loaded with weapons.",
              None, None, None, None, "west", None, None, None, ["Assault Rifle",
                                                                 'Backpack', 'Shotgun', 'SemiAutoSniper'])
living = Room('Living Room', 'There are two couches in the middle of the room and a TV with the screen facing the '
                             'couches. There is a door at the Northeast corner of the room and a hallway leading to'
                             ' the front door.', None, "front", None, "west", None, None, "kitchen", None, [])
front = Room("Front Door", "There is a dark oak wooden door, the "
                           "Living Room is right behind you.", "living", "porch",
             None, None, None, None, None, None, [])
kitchen = Room("Kitchen", "There is a table in the middle of the room with chairs surrounding it."
                          " There is also food sitting on the counter. There is a door to"
               " the Southeast corner of the room and another door leading back to the Living Room to the south", None,
               "living", None, None, None, None, None, "bed", ['Food'])
bed = Room("Bed Room", "There is a bed next the side wall, there is a night stand next to it and a desk on the other"
                       " side of the room with a window.", "kitchen",
           "rest", None, "bed2", "attic", None, None, None, ['Healing Potion'])
bed2 = Room("Bed Room 2", "It looks the same as the other bedroom except there"
                          " is no window.", None, None, "bed", None, None, None, None, None, ['Knife'])
rest = Room("Restroom", "There is a toilet and a shower at the far back and a sink with a mirror "
                        "on the side.", "bed", None, None, None, None, None, None, None, ["Bandages"])
attic = Room("Attic", "There are a lot of dusty boxes that are pushed to the back. The ceiling is also very low."
                      " You notice a knife on top of one of the boxes.",
             None, None, None, None, None, "bed", None, None, ['Crossbow'])
porch = Room("Porch", "You go outside and the sun is really bright, you close the door behind you. The porch is very"
                      " small, there is a hammock to the left of you and a grill to the right. There is also a street"
                      " in front of you and what looks like a park in the distance.",
             "front", "street", "garage", None, None, None, None, None, [])
garage = Room("Garage", "The garage is small, there is no car inside. There are empty, dusty shelves"
                        " all across the walls.", None, "street2", "porch",
              None, None, None, None, None, ['Shotgun', 'Healing Potion'])
street = Room("Street", "You are on the street in front of the house, on the east there is street, and at west there"
                        " is more street", "porch", "park", "street2", "street3", None, None, None, None, [])
street2 = Room("East Street", "To the east, it looks like there is a gate to what seems to be a"
                              " neighborhood, to the west... more"
                              " street", "garage", None, "neighborhood_gate", "street", None, None, None, None, [])
street3 = Room("West Street", "To the west... more street. To "
                              "the east... more street", None, None, "street", "street4", None, None, None, None, [])
street4 = Room("West Street 2", "To the east... more street. To the west, it looks like there is a gate"
                                " to what "
                                "seems to be a town", None, None, "street3", "town_gate", None, None, None, None, [])
town_gate = Room("Town Gate", "The gate seems to be locked, with no other way around it. "
                              "To the east... more street.", None, None, "street4", None, None, None, None, None, [])
neighborhood_gate = Room("Neighborhood Gate", "The gate seems to be locked, with no other way around it. "
                                              "To the west... "
                                              "more street.", None, None, None, 'street2', None, None, None, None, [])
park = Room("Park", 'The park gate is unlocked, to the north, street. To the south, there is an old'
                    ' playground.', 'street', 'playground', None, None, None, None, None, None, ['axe'])
playground = Room('Playground', "All of the things on the playground seem to be "
                                "old. To the north, the park gate. "
                                "To the south a gate to a pond. To the east, a building that says restrooms. "
                                "To the west, another gated area.", 'park', 's_gated_area', 'restrooms', 'w_gated_area',
                  None, None, None, None, [])
s_gated_area = Room('South Gated Area', 'The gate to the pond seems to be locked. To the north, the playground.',
                    'playground', 'pond', None, None, None, None, None, None, [])
pond = Room('Pond', 'There is a pond that is full of algae and the water is really dirty. To the north the playground.',
            'playground', None, None, None, None, None, None, None, ['Axe'])
w_gated_area = Room('West Gated Area', 'The gate seems to be locked, there is not really anything to gate up.'
                                       ' To the east, the playground', None, None, 'playground', None, None, None, None,
                    None, [])
restrooms = Room('Park Restrooms', 'There are dirty old restrooms that stink. Inside there is ... Food?'
                                   ' To the east, the playground.', None, None,
                 None, 'playground', None, None, None, None, ['Food', 'KeyToPond'])


current_node = spawn
directions = ['south', 'north', 'east', 'west', 'down', 'up', 'northeast', 'southeast']
short_directions = ['s', 'n', 'e', 'w', 'd', 'u', 'ne', 'se']

print(current_node.name + '\n' + current_node.description)
while True:
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    elif command == 'pew pew':
        print('The house blew up and you died')
        quit(0)
    elif command == "look":
        print(current_node.name, '\n', current_node.description)
    elif command == 'yote':
        quit("past tense of yeet")
    else:
        print("Command not recognized")

    if command in directions:
        try:
            current_node.move(command)
            print(current_node.name + "\n" + current_node.description)
        except KeyError:
            print("You cannot go this way")