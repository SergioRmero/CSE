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
secret = Room("Secret Room", "This is a dark room with what seems to"
                             "be loaded with weapons.", None, None, None, None, "west", None, None, None)
living = Room('Living Room', 'There are two couches in the middle of the room and a TV with the screen facing the'
                             'couches. There is a door at the Northeast corner of the room and a hallway leading to'
                             'the front door.', None, "front", None, "west", None, None, "kitchen", None)
front = Room("Front Door", "There is a dark oak wooden door, the "
                           "Living Room is right behind you.", "living", "porch", None, None, None, None, None, None)
kitchen = Room("Kitchen", "There is a table in the middle of the room with chairs surrounding it. There is a door to"
               "the Southeast corner of the room and another door leading back to the Living Room to the south", None,
               "living", None, None, None, None, None, "bed")
bed = Room("Bed Room", "There is a bed on the side wall, there is a night stand next to it and a desk on the other"
                       "side of the room with a window.", "kitchen", "rest", None, "bed2", "attic", None, None, None)
bed2 = Room("Bed Room 2", "It looks the same as the other bedroom except there"
                          " is no window.", None, None, "bed", None, None, None, None, None)
rest = Room("Restroom", "There is a toilet and a shower at the far back and a sink with a mirror "
                        "on the side.", "bed", None, None, None, None, None, None, None)
attic = Room("Attic", "There are a lot of dusty boxes that are pushed to the back. The ceiling is also very low."
                      "You notice a knife on top of one of the boxes.", None, None, None, None, None, "bed", None, None)
porch = Room("Porch", "None yet", "front", "street", "garage", None, None, None, None, None)
garage = Room("Garage", "The garage is small, there is no car inside. There are empty, dusty shelves"
                        " all across the walls.", None, "street2", "porch", None, None, None, None, None)
street = Room("Street", "You are on the street in front of the house, on the east there is street, and at west there"
                        " is more street", "porch", "park", "street2", "street3", None, None, None, None)
street2 = Room("East Street", "To the east, it looks like there is a gate to what seems to be a"
                              " neighborhood, to the west... more"
                              "street", "garage", None, "neighborhood_gate", "street", None, None, None, None)
street3 = Room("West Street", "To the west... more street. To "
                              "the east... more street", None, None, "street", "street4", None, None, None, None)
street4 = Room("West Street 2", "To the east... more street. To the west, it looks like there is a gate"
                                " to what "
                                "seems to be a town", None, None, "street3", "town_gate", None, None, None, None)
town_gate = Room("Town Gate", "The gate seems to be locked, with no other way around it. To the east... more street."
                 , None, None, "West Street 2", None, None, None, None, None)
neighborhood_gate = Room("Neighborhood Gate", "The gate seems to be locked, with no other way around it. "
                                              "To the west... more street."
                         , None, None, None, 'East Street', None, None, None, None)
park = Room("Park", 'The park gate is unlocked, to the north, street. To the south, there is an old playground.'
            , 'street', 'playground', None, None, None, None, None, None)
playground = Room('Playground', "All of the things on the playground seem to be "
                                "old. To the north, the park gate. "
                                "To the south a gate to a pond. To the east, a building that says restrooms. "
                                "To the west, another gated area.", 'park', 's_gated_area', 'restrooms', 'w_gated_area')
s_gated_area = Room('South Gated Area', 'The gate to the pond seems to be locked. To the north, the playground.',
                    'playground', 'pond', None, None, None, None, None, None)
pond = Room('Pond', 'There is a pond that is full of algae and the water is really dirty. To the north the playground.',
            'park', None, None, None, None, None, None, None)
w_gated_area = Room()


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
