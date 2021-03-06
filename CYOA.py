import random as rand


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


class SteelSword(Melee):
    def __init__(self, name, description, damage_dealt, is_picked, room, used):
        self.enemy_health = 100
        super(SteelSword, self). __init__(name, description, damage_dealt, is_picked, room, used)

    def attack(self):
        damage_dealt = 50
        self.enemy_health -= damage_dealt
        print('You attack with %s' % self.name)


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


class Food(Consumable):
    def __init__(self, name, description, hunger_restored, is_picked, room, used):
        self.hunger = hunger_restored
        super(Food, self). __init__(name, description, hunger_restored, is_picked, room, used)

    def eat(self):
        print("You ate %s and restored %d hunger" % (self.name, self.hunger))


class Healing(Consumable):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(Healing, self). __init__(name, description, None, is_picked, room, used)
        self.health_restored = health_restored

    def heal(self):
        global health
        health += self.health_restored


class Bandages(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(Bandages, self). __init__(name, description, None, is_picked, room, used)
        self.health_restored = health_restored

    def heal(self):
        global health
        health += self.health_restored
        print("You healed %d hp with %s" % (self.health_restored, self.name))


class HealingPotion(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        self.health = 100
        super(HealingPotion, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self):
        global health
        health += self.health_restored
        print("You healed %d hp with %s" % (self.health_restored, self.name))


class PainKillers(Healing):
    def __init__(self, name, description, health_restored, is_picked, room, used):
        super(PainKillers, self). __init__(name, description, health_restored, is_picked, room, used)

    def heal(self):
        global health
        health += self.health_restored
        print('You healed %d hp with %s' % (self.health_restored, self.name))


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


class Enemy(Characters):
    def __init__(self, name, description, health, room, item_drop):
        self.room = room
        self.item = item_drop
        super(Enemy, self). __init__(name, description, health)

    def attack(self, damage):
        self.health -= damage
        print("%s attacked you" % self.name)

    def death(self, cause):
        print("%s was killed by your %s" % (self.name, cause.name))
        if self.item is not None:
            self.item.is_picked = False
            print("%s dropped %s" % (self.name, self.item.name))


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
spawn_clos = Room('Closet', 'You are in a closet that has many supplies for.', None, spawn, None, None, None, None,
                  None, None)
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
                          " There is also some food sitting on the counter. There is a door to"
               " the Southeast corner of the room and another\ndoor leading back to the Living Room to the south", None,
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
             "front", "street", 'garage', None, None, None, None, None)
garage = Room("Garage", "The garage is small, there is no car inside. There are empty, dusty shelves"
                        " all across the walls.", None, "street2", None,
              'porch', None, None, None, None)
street = Room("Street", "You are on the street in front of the house, on the east there is street, and at west there"
                        " is more street, there is also a zombie coming towards you.", "porch", "park", "street2",
                        "street3", None, None, None, None)
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

crossbow = Crossbow('crossbow', 'It looks like a crossbow, when it fires the arrow goes very far', 55, False,
                    garage, False)
steel_sword = SteelSword('Steel Sword', 'A nice shiny sword that looks very sharp', 50, False, spawn_clos, False)
pistol = Pistol('pistol', 'You picked up a pistol.', 15, False, bed, False)
shotgun = Shotgun('shotgun', 'You picked up a shotgun, is more effective at close range.', 70,
                  False, secret, False)
assault_rifle = AssaultRifle('assault rifle', 'You picked up an assault rifle.', 40, False, secret, False)
snipe = Sniper('sniper', 'A sniper, this does more damage than the crossbow', 65, False, secret, False)
axe = Axe('axe', 'You picked up an axe, does not do a lot of damage.', 15, False, pond,
          False)
knife = Knife('knife', 'You picked up a knife, does the least damage out of all the weapons', 10, False, attic, False)
food = Food('Food', 'You picked up a bag. There is food in a bag, the bag also feels warm. This restores 25 hunger',
            20, False, kitchen, False)
food2 = Food('Food', 'You picked up a bag. There is food in a bag, the bag also feels warm. This restores 25 hunger',
             20, False, restrooms, False)
food3 = Food('beesechurger', 'chinken nunget', 30, True, pond, False)
food4 = Food('chicken strips', 'Food', 20, True, street, False)
food5 = Food('prunes', 'Food', 20, True, street2, False)
food6 = Food('boneless pizza', "It don't got no bone in it", 25, True, street3, False)
food7 = Food('chick fil a', 'is not open on Sundays', 15, True, street4, False)
food8 = Food('sandwich', 'You picked up a bag. This restores 25 hunger', 20, True, park, False)
food9 = Food('donut', 'This restores 25 hunger', 20, True, playground, False)
food10 = Food('expired milk', 'You picked up a bag. This restores 5 hunger',
              20, True, s_gated_area, False)
food11 = Food('bean burrito', 'You picked up a bag. There is food in a bag, the bag also feels warm.'
                              ' This restores 25 hunger', 20, True, w_gated_area, False)
bandages = Bandages('bandages', 'You picked up bandages, these restore 10 health to you', 10, False, rest, False)
bandages2 = Bandages('Bandages', 'You picked up bandages, these restore 10 health to you', 10, False, restrooms, False)
healing_pot = HealingPotion('healing potion', 'You picked a healing potion. This potion restores 25 health to you.',
                            25, False, bed, False)
healing_pot2 = HealingPotion('Healing potion', 'You picked a healing potion. This potion restores 25 health to you.',
                             25, False, garage, False)
painkillers = PainKillers('pain killers', 'These restore 45 hp', 45, False, rest, False)
painkillers2 = PainKillers('Pain killers', "These restore 45 hp", 45, False, porch, False)
painkillers3 = PainKillers('Pain killers', "These restore 45 hp", 45, False, porch, False)
user = User('Player', 'You are an average person not knowing a lot about what is around him.', 100, 10)
enemy1 = Enemy('Zombie', 'One of many zombies', 200, pond, food3)
enemy2 = Enemy('Zombie', 'One of many zombies', 100, street, food4)
enemy3 = Enemy('Zombie', 'One of many zombies', 150, street2, food5)
enemy4 = Enemy('Zombie', 'One of many zombies', 85, street3, food6)
enemy5 = Enemy('Zombie', 'One of many zombies', 50, street4, food7)
enemy6 = Enemy('Zombie', 'One of many zombies', 85, park, food8)
enemy7 = Enemy('Zombie', 'One of many zombies', 80, playground, food9)
enemy8 = Enemy('Zombie', 'One of many zombies', 123, s_gated_area, food10)
enemy9 = Enemy('Zombie', 'One of many zombies', 420, w_gated_area, food11)

item_list = [bandages, assault_rifle, snipe, healing_pot, food, axe, shotgun, pistol, crossbow,
             knife, food2, healing_pot2, food3, food4, food5, food6, food7, food8, food9, food10, food11,
             bandages2, painkillers, painkillers2, painkillers3, ]
enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9]
current_node = spawn
directions = ['south', 'north', 'east', 'west', 'down', 'up', 'northeast', 'southeast']
short_directions = ['s', 'n', 'e', 'w', 'd', 'u', 'ne', 'se']

sib = 10
health = 100
hunger = 100
main = None
inventory = []

dead_items = []

ii = isinstance
print('Type "tutorial" to see tutorial')
print(current_node.name + '\n' + current_node.description + '\n' + 'Health = %s' % health + '\n' + 'Hunger = %s'
      % hunger)
while health > 0:
    accuracy = rand.randint(0, 2)
    if health > 100:
        health = 100
    elif hunger > 100:
        hunger = 100
    elif hunger < 0:
        hunger = 0
        health -= 10
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command == 'tutorial':
        print("Welcome!\n\nTo move rooms type the direction you want to go in.\nFor example, type n to go north,"
              " e to go east, etc.\n\nType 'look' to see what room you're in.\nType 'items' to see what items are in a "
              "room. \nTo take items, type 'take' and the item you want to pick up.\nTo drop items, type 'drop' and the"
              " item you want to drop.\nTo see what items you have in your inventory type 'inventory'. \nTo see your "
              "health and hunger type 'stats'.\nTo heal, type 'heal with' and the item you want to heal with.\nTo eat, "
              "type 'eat' and the item you want to eat.\n\nThere are zombies in this game, so you will want to obtain"
              " some weapons.\nTo shoot type 'shoot zombie', you will need to equip the gun before you are able to use"
              " it.\nTo attack with a melee weapon type 'attack zombie with', and the melee weapon you want to attack "
              "with.\nAnd finally, to quit playing the game type 'quit' and the game will stop running.\nGood luck!")
    elif command == "items":
        __item = False
        for _item in item_list:
            if _item.room is not current_node:
                __item = False
            else:
                __item = True
                print("- " + _item.name)
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
        b = Bandages
        hp = HealingPotion
        pk = PainKillers
        item = None
        for _item in inventory:
            if str.lower(_item.name) in command:
                item = _item
        if ii(item, b) or ii(item, hp) or ii(item, pk):
            item.heal()
            inventory.remove(item)
            dead_items.append(item)
    elif 'shoot' in command:
        for enemy in enemy_list:
            if str.lower(enemy.name) in command and enemy.room is current_node:
                if main is None:
                    print("You don't have a weapon")
                else:
                    zombie_damage = rand.randint(15, 25)
                    if accuracy is 0:
                        health -= zombie_damage
                        print("You missed the shot so the zombie took advantage and attacked you.")
                        print('Health = %s' % health)
                    else:
                        enemy.health -= main.damage_dealt
                        main.shoot(enemy)
                if enemy.health <= 0:
                    enemy.room = None
                    enemy.death(main)
                    enemy_list.remove(enemy)
                    dead_items.append(enemy)
    elif 'attack zombie with' in command:
        ii = isinstance
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked:
                if ii(_item, Axe) or ii(_item, Knife):
                    zombie_damage = rand.randint(15, 25)
                    accuracy = rand.randint(0, 2)
                    if accuracy is 0:
                        print("You missed")
                    else:
                        _item.attack()
    elif 'eat' in command:
        ii = isinstance
        for _item in inventory:
            if str.lower(_item.name) in command and _item.is_picked and ii(_item, Food):
                hunger += _item.hunger
                _item.eat()
                inventory.remove(_item)
                dead_items.append(_item)
    elif command == 'stats':
        print("Health = %s" % health + "\n" + "Hunger = %s" % hunger)
    else:
        atk = False
        for enemy in enemy_list:
            if enemy.room is current_node:
                zombie_damage = rand.randint(15, 25)
                health -= zombie_damage
                print("You stumbled, and the %s attacked you." % str.lower(enemy.name))
                atk = True
        if not atk:
            print("Command not recognized")
    if command in directions:
        try:
            current_node.move(command)
            print(current_node.name + "\n" + current_node.description + '\n' + 'Health = %s' % health + '\n' +
                  'Hunger = %s' % hunger)
        except KeyError:
            print("You cannot go this way")
    hunger -= 0.5
