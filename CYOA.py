class Item(object):
    def __init__(self, name, description, is_picked, room, used):
        self.name = name
        self.description = description
        self.is_picked = is_picked
        self.room = room
        self.used = used

    def drop(self, room):
        if self.is_picked:
            self.is_picked = False
            self.room = room
            print("You dropped %s" % self.name)
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

    def shoot(self, target):
        print("You shoot %s with your %s" % (str.lower(target.name), str.lower(self.name)))


class Melee(Weapons):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        super(Melee, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        print("You attack with %s" % self.name)


class Crossbow(Ranged):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(Crossbow, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self, target):
        print("You shoot %s with your %s" % (str.lower(target.name), str.lower(self.name)))


class Guns(Ranged):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(Guns, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self, target):
        print("You shoot %s with your %s" % (str.lower(target.name), str.lower(self.name)))


class Pistol(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(Guns, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self, target):
        print("You shoot %s with your %s" % (str.lower(target.name), str.lower(self.name)))


class Shotgun(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(Shotgun, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self, target):
        print("You shoot %s with your %s" % (str.lower(target.name), str.lower(self.name)))


class AssaultRifle(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(AssaultRifle, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self, target):
        print("You shoot %s with your %s" % (str.lower(target.name), str.lower(self.name)))


class Sniper(Guns):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(Sniper, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def shoot(self, target):
        print("You shoot %s with your %s" % (str.lower(target.name), str.lower(self.name)))


class Axe(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(Axe, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        damage_dealt = 15
        self.enemy_health -= damage_dealt
        print("You attack with %s" % self.name)


class Knife(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(Knife, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        damage_dealt = 10
        self.enemy_health -= damage_dealt
        print("You attack with %s" % self.name)


class Backpack(Wearable):
    def __init__(self, name, description, storage, is_picked, room, used, worn):
        self.worn = worn
        super(Backpack, self). __init__(name, description, storage, is_picked, room, used)

    def wear(self):
        if not self.worn:
            self.worn = True
            print("You are wearing %s" % self.name)
        else:
            print("You're already wearing the %s" % str.lower(self.name))

    def off(self):
        if self.worn:
            self.worn = False
            print("You took off %s" % self.name)
        else:
            print("You are not wearing %s" % self.name)


class Food(Consumable):
    def __init__(self, name, description, hunger_restored, is_picked, room, used):
        self.hunger = 100
        super(Food, self). __init__(name, description, hunger_restored, is_picked, room, used)

    def eat(self, hunger_restored):
        self.hunger += hunger_restored
        print("You ate %s and restored %d hunger" % (self.name, hunger_restored))


class Healing(Consumable):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        self.health = 100
        super(Healing, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self, heal_amount):
        self.health += heal_amount


class Bandages(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        self.health = 100
        super(Bandages, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self, heal_amount):
        heal_amount = 10
        self.health += heal_amount
        print("You healed 10 hp with %s" % self.name)


class HealingPotion(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        self.health = 100
        super(HealingPotion, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self, heal_amount):
        heal_amount = 25
        self.health += heal_amount
        print("You healed 25 hp with %s" % self.name)


class Characters(object):
    def __init__(self, name, description, health):
        self.name = name
        self.description = description
        self.health = health


class User(Characters):
    def __init__(self, name, description, health, inventory):
        self.space = inventory
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
    def __init__(self, name, description, north, south, east, west, up, down, northeast, southeast):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# north, south, east, west, up , down, northeast, southeast
spawn = Room("Spawn", 'You are in an empty room with the ceiling light dimly lit.'
             ' There is an open door at the south side of the room',
             None, "west", None, None, None, None, None, None)
west = Room("West Room", "There is a door on the east side of the room and a trap door on the floor that seems to be"
            " unlocked", "spawn", None, "living", None, None, "secret", None, None)
secret = Room("Secret Room", "This is a dark room with what seems to"
                             " be loaded with weapons.",
              None, None, None, None, "west", None, None, None)
living = Room('Living Room', 'There are two couches in the middle of the room and a TV with the screen facing the '
                             'couches. There is a door at the Northeast corner of the room and a hallway leading to'
                             ' the front door.', None, "front", None, "west", None, None, "kitchen", None)
front = Room("Front Door", "There is a dark oak wooden door, the "
                           "Living Room is right behind you.", "living", "porch",
             None, None, None, None, None, None)
kitchen = Room("Kitchen", "There is a table in the middle of the room with chairs surrounding it."
                          " There is also food sitting on the counter. There is a door to"
               " the Southeast corner of the room and another door leading back to the Living Room to the south", None,
               "living", None, None, None, None, None, "bed")
bed = Room("Bed Room", "There is a bed next the side wall, there is a night stand next to it and a desk on the other"
                       " side of the room with a window. There is a bottle with red liquid and a pistol on the desk",
           "kitchen", "rest", None, "bed2", "attic", None, None, None)
bed2 = Room("Bed Room 2", "It looks the same as the other bedroom except there"
                          " is no window.", None, None, "bed", None, None, None, None, None)
rest = Room("Restroom", "There is a toilet and a shower at the far back and a sink with a mirror "
                        "on the side.", "bed", None, None, None, None, None, None, None)
attic = Room("Attic", "There are a lot of dusty boxes that are pushed to the back. The ceiling is also very low."
                      " You notice a knife on top of one of the boxes.",
             None, None, None, None, None, "bed", None, None)
porch = Room("Porch", "You go outside and the sun is really bright, you close the door behind you. The porch is very"
                      " small, there is a hammock to the left of you and a grill to the right. There is also a street"
                      " in front of you and what looks like a park in the distance.",
             "front", "street", "garage", None, None, None, None, None)
garage = Room("Garage", "The garage is small, there is no car inside. There are empty, dusty shelves"
                        " all across the walls.", None, "street2", "porch",
              None, None, None, None, None)
street = Room("Street", "You are on the street in front of the house, on the east there is street, and at west there"
                        " is more street", "porch", "park", "street2", "street3", None, None, None, None)
street2 = Room("East Street", "To the east, it looks like there is a gate to what seems to be a"
                              " neighborhood, to the west... more"
                              " street", "garage", None, "neighborhood_gate", "street", None, None, None, None)
street3 = Room("West Street", "To the west... more street. To" 
                              "the east... more street", None, None, "street", "street4", None, None, None, None)
street4 = Room("West Street 2", "To the east... more street. To the west, it looks like there is a gate"
                                " to what "
                                "seems to be a town", None, None, "street3", "town_gate", None, None, None, None)
town_gate = Room("Town Gate", "The gate seems to be locked, with no other way around it. "
                              "To the east... more street.", None, None, "street4", None, None, None, None, None)
neighborhood_gate = Room("Neighborhood Gate", "The gate seems to be locked, with no other way around it. "
                                              "To the west... "
                                              "more street.", None, None, None, 'street2', None, None, None, None)
park = Room("Park", 'The park gate is unlocked, to the north, street. To the south, there is an old'
                    ' playground.', 'street', 'playground', None, None, None, None, None, None)
playground = Room('Playground', "All of the things on the playground seem to be "
                                "old. To the north, the park gate. "
                                "To the south a gate to a pond. To the east, a building that says restrooms. "
                                "To the west, another gated area.", 'park', 's_gated_area', 'restrooms', 'w_gated_area',
                  None, None, None, None)
s_gated_area = Room('South Gated Area', 'The gate to the pond seems to be locked. To the north, the playground.',
                    'playground', 'pond', None, None, None, None, None, None)
pond = Room('Pond', 'There is a pond that is full of algae and the water is really dirty. To the north the playground.',
            'playground', None, None, None, None, None, None, None)
w_gated_area = Room('West Gated Area', 'The gate seems to be locked, there is not really anything to gate up.'
                                       ' To the east, the playground', None, None, 'playground', None, None, None, None,
                    None)
restrooms = Room('Park Restrooms', 'There are dirty old restrooms that stink. Inside there is ... Food?'
                                   ' To the east, the playground.', None, None,
                 None, 'playground', None, None, None, None)

Key_To_Pond = Item('key to pond', 'You picked up a key to the pond', False, restrooms, False)
crossbow = Crossbow('crossbow', 'It looks like a crossbow, when it fires the arrow goes very far', 50, False,
                    garage, False)
pistol = Pistol('pistol', 'You picked up a pistol.', 15, False, bed, False)
shotgun = Shotgun('shotgun', 'You picked up a shotgun, is more effective at close range.', 70,
                  False, secret, False)
assault_rifle = AssaultRifle('assault rifle', 'You picked up an assault rifle.', 40, False, secret, False)
snipe = Sniper('sniper', 'A sniper, this does more damage than the crossbow', 65, False, secret, False)
axe = Axe('axe', 'You picked up an axe, does not do a lot of damage.', 15, False, pond,
          False)
knife = Knife('knife', 'You picked up a knife, does the least damage out of all the weapons', 10, False, attic, False)
backpack = Backpack('backpack', 'You picked up a backpack, you could probably put some items in here.', 10, False,
                    secret, False, False)
food = Food('food', 'You picked up a bag. There is food in a bag, the bag also feels warm. This restores 25 hunger',
            20, False, kitchen, False)
food2 = Food('food', 'You picked up a bag. There is food in a bag, the bag also feels warm. This restores 25 hunger',
             20, False, restrooms, False)
bandages = Bandages('bandages', 'You picked up bandages, these restore 30 health to you', 30, False, rest, False)
healing_pot = HealingPotion('healing potion', 'You picked a healing potion. This potion restores 50 health to you.',
                            50, False, bed, False)
healing_pot2 = HealingPotion('healing potion', 'You picked a healing potion. This potion restores 50 health to you.',
                             50, False, garage, False)
user = User('Player', 'You are an average person not knowing a lot about what is around him.', 100, 10)
enemy1 = Enemy('Zombie', 'One of many zombies', 200, pond, 'food')
enemy2 = Enemy('Zombie', 'One of many zombies', 200, street, 'food')
enemy3 = Enemy('Zombie', 'One of many zombies', 150, street2, 'food')
enemy4 = Enemy('Zombie', 'One of many zombies', 85, street3, 'food')
enemy5 = Enemy('Zombie', 'One of many zombies', 50, street4, 'food')
enemy6 = Enemy('Zombie', 'One of many zombies', 85, park, 'food')
enemy7 = Enemy('Zombie', 'One of many zombies', 80, playground, 'food')
enemy8 = Enemy('Zombie', 'One of many zombies', 123, s_gated_area, 'food')
enemy9 = Enemy('Zombie', 'One of many zombies', 420, w_gated_area, 'food')

item_list = [bandages, assault_rifle, snipe, healing_pot, food, axe, shotgun, pistol, crossbow, Key_To_Pond,
             knife, backpack, food2, healing_pot2]
enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9]

current_node = spawn
directions = ['south', 'north', 'east', 'west', 'down', 'up', 'northeast', 'southeast']
short_directions = ['s', 'n', 'e', 'w', 'd', 'u', 'ne', 'se']

sib = 10
health = 100
hunger = 100
main = None
inventory = []

nil = []

ii = isinstance

print(current_node.name + '\n' + current_node.description + '\n' + 'Health = %s' % health + '\n' + 'Hunger = %s'
      % hunger)
while health != 0:
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command == "items":
        __item = False
        for _item in item_list:
            if _item.room is not current_node:
                __item = False
            else:
                __item = True
                print("- " + _item.name)
        if not __item:
            print("There are no items in the room.")
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    elif "take" in command:
        for _item in item_list:
            if str.lower(_item.name) in command and not _item.is_picked and _item.room is current_node:
                item_list.remove(_item)
                inventory.append(_item)
                sg = Shotgun
                ar = AssaultRifle
                s = Sniper
                cb = Crossbow
                p = Pistol
                if ii(_item, sg) or ii(_item, ar) or ii(_item, s) or ii(_item, cb) or ii(_item, p):
                    print("You picked up the %s but you need to equip it before you use it." % str.lower(_item.name))
                else:
                    _item.pick()
            elif "all" in command and _item.room is current_node:
                item_list.remove(_item)
                inventory.append(_item)
                sg = Shotgun
                ar = AssaultRifle
                s = Sniper
                cb = Crossbow
                p = Pistol
                if ii(_item, sg) or ii(_item, ar) or ii(_item, s) or ii(_item, cb) or ii(_item, p):
                    print("You picked up the %s but you need to equip it before you use it." % str.lower(_item.name))
                else:
                    _item.pick()
    elif 'drop' in command:
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked:
                _item.drop(current_node)
                inventory.remove(_item)
                item_list.append(_item)
    elif "wear" in command:
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked:
                if isinstance(_item, Backpack):
                    _item.wear()
                else:
                    print("You can't wear %s" % _item.name)
    elif "remove" in command:
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked:
                if isinstance(_item, Backpack):
                    _item.off()
    elif "equip" in command:
        for _item in inventory:
            if str.lower(_item.name) in command and _item.pick:
                sg = Shotgun
                ar = AssaultRifle
                s = Sniper
                cb = Crossbow
                p = Pistol
                if ii(_item, sg) or ii(_item, ar) or ii(_item, s) or ii(_item, cb) or ii(_item, p):
                    if main is not None:
                        main = None
                        main = _item
                    else:
                        main = _item
                    print("You equipped the %s" % str.lower(_item.name))
    elif "unequip" in command:
        for _item in inventory:
            if str.lower(_item.name) in command and _item.pick:
                sg = Shotgun
                ar = AssaultRifle
                s = Sniper
                cb = Crossbow
                p = Pistol
                if ii(_item, sg) or ii(_item, ar) or ii(_item, s) or ii(_item, cb) or ii(_item, p):
                    if main is not None:
                        main = None
                        print("You unequipped the %s" % str.lower(_item.name))
                    else:
                        print("You can't unequip anything.")
    elif command == 'inventory':
        for _item in inventory:
            print(_item.name)
    elif command == "look":
        print(current_node.name + '\n' + current_node.description)
        print("Current items in the room :")
        for _item in item_list:
            if _item.room == current_node:
                print("- " + _item.name)
    elif 'heal with' in command:
        ii = isinstance
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked and ii(_item, Bandages) or ii(_item, HealingPotion):
                _item.heal(current_node)
                inventory.remove(_item)
                nil.append(_item)
        else:
            print('Command not recognized.')
    elif 'shoot' in command:
        for enemy in enemy_list:
            if str.lower(enemy.name) in command and enemy.room is current_node:
                enemy.health -= main.damage_dealt
                main.shoot(enemy)
        for enemy in enemy_list:
            if enemy.room is current_node and enemy.health <= 0:
                enemy.room = None
                enemy_list.remove(enemy)
                nil.append(enemy)
                print("You killed %s" % str.lower(enemy.name))

    elif 'attack zombie with' in command:
        ii = isinstance
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked:
                if ii(_item, Axe) or ii(_item, Knife):
                    _item.attack()

    elif 'eat' in command:
        ii = isinstance
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked and ii(_item, Food):
                _item.eat(20)
                inventory.remove(_item)
                nil.append(_item)
    else:
        print("Command not recognized")
    if command in directions:
        try:
            current_node.move(command)
            print(current_node.name + "\n" + current_node.description + '\n' + 'Health = %s' % health + '\n' +
                  'Hunger = %s' % hunger)
        except KeyError:
            print("You cannot go this way")
