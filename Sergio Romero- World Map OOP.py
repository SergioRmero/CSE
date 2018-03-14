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
             'There is an open door at the south side of the room', None, "west", None, None, None, None, None, None)
west = Room("West Room", "There is a door on the east side of the room and a trap door on the floor that seems to be"
            "locked", "Spawn", None, "living", None, None, "secret", None, None)
secret = Room("Secret Room", "none yet", None, None, None, None, "west", None, None, None)
living = Room('Living Room', 'There are two couches in the middle of the room and a TV with the screen facing the'
                             'couches. There is a door at the Northeast corner of the room and a hallway leading to'
                             'the front door.', None, "front", None, "west", None, None, "kitchen", None)
front = Room("Front Door", "none yet", "living", "porch", None, None, None, None, None, None)
kitchen = Room("Kitchen", "There is a table in the middle of the room with chairs surrounding it. There is a door to"
               "the Southeast corner of the room and another door leading back to the Living Room to the south", None,
               "living", None, None, None, None, None, "bed")
bed = Room("Bed Room", "no description yet", "kitchen", "rest", None, "bed2", "attic", None, None, None)
bed2 = Room("Bed Room 2", "NO DESCRIPTION YET", None, None, "bed", None, None, None, None, None)
rest = Room("Restroom", "NO DESCRIPTION YET", "bed", None, None, None, None, None, None, None)
attic = Room("Attic", "NO DESCRIPTION YET", None, None, None, None, None, "bed", None, None)
porch = Room("Porch", "None yet", "front", "street", "garage", None, None, None, None, None)
garage = Room("Garage", "None yet", None, "street2", "porch", None, None, None, None, None)
street = Room("Street", "You are on the street in front of the house, on the east there is street, and at west there"
                        " is more street", "porch", "park", "street2", "street3", None, None, None, None)
street2 = Room("East Street", "None yet", "garage", None, "neighborhood_gate", "street", None, None, None, None)
street3 = Room("West Street", "None yet", None, None, "street", "street4", None, None, None, None)
street4 = Room("West Street 2", "None yet", None, None, "street3", "town_gate", None, None, None, None)
town_gate = Room("Town Gate", "None yet", None, None, "West Street 2", None, None, None, None, None)
neighborhood_gate = Room("Neighborhood Gate", "None yet", None, None, None, 'East Street', None, None, None, None)

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
    if command in directions:
        try:
            current_node.move(command)
            print(current_node.name + "\n" + current_node.description)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
