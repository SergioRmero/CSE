world_map = {
    'SPAWN': {
        'NAME': 'SPAWN',
        'DESCRIPTION': 'You are in an empty room with the ceiling light dimly lit. '
                       'There is an open door at the south side of the room',
        'PATHS': {
            'SOUTH': 'WEST ROOM',
            'NORTH': 'SPAWN'
        }
    },
    'WEST ROOM': {
        'NAME': 'West Room',
        'DESCRIPTION': "There is a door on the east side of the room and a trap door on the floor that seems to be "
                       "locked",
        'PATHS': {
            'EAST': 'LIVING ROOM',
            'DOWN': 'SECRET ROOM',
            'NORTH': 'SPAWN'
        }
    },
    'LIVING ROOM': {
        'NAME': 'Living Room',
        'DESCRIPTION': 'There are two couches in the middle of the room and a TV with the screen facing the couches'
                       'There is a door at the North East corner of the room and a hallway leading to the front door'
                       'of the house',
        'PATHS': {
            'NORTHEAST': 'KITCHEN',
            'SOUTH': 'FRONT DOOR',
            'WEST': 'WEST ROOM'
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'There is a table in the middle of the room with chairs surrounding it. There is also a kitchen'
                       'counter with all the basic kitchen utilities. There is a door at the South East corner of the'
                       'room and a door leading back to the Living Room',
        'PATHS': {
            'SOUTHEAST': 'BED ROOM',
            'SOUTH': 'LIVING ROOM'
        }
    },
    'BED ROOM': {
        'NAME': 'Bed Room',
        'DESCRIPTION': 'There is a bed on the side wall, there is a night stand next to it and a desk on the other'
                       'side of the room with a window.',
        'PATHS': {
            'UP': 'ATTIC',
            'SOUTH': 'RESTROOM',
            'WEST': 'BED ROOM 2',
            'NORTH': 'KITCHEN'
        }
    },
    'BED ROOM 2': {
        'NAME': 'Bed Room 2',
        'DESCRIPTION': 'It looks the same as the other bedroom except there is no window.',
        'PATHS': {
            'EAST': 'BED ROOM'
        }
    },
    'RESTROOM': {
        'NAME': 'Restroom',
        'DESCRIPTION': 'There is a toilet and a shower at the far back and a sink with a mirror on the side.',
        'PATHS': {
            'SOUTH': 'BED ROOM'
        }
    },
    'ATTIC': {
        'NAME': 'Attic',
        'DESCRIPTION': 'There are a lot of dusty boxes that are pushed to the back. The ceiling is also very low.'
                       'You notice a knife on top of one of the boxes.',
        'PATHS': {
            'DOWN': 'BED ROOM'
        }
    },
    'FRONT DOOR': {
        'NAME': 'Front Door',
        'DESCRIPTION': 'There is a dark oak wooden door, the Living Room is right behind you.',
        'PATHS': {
            'NORTH': 'LIVING ROOM',
            'SOUTH': 'PORCH'
        }
    },
    'PORCH': {
        'NAME': 'Porch',
        'DESCRIPTION': 'You go outside and the sun is really bright, you close the door behind you. The porch is very'
                       'small, there is a hammock to the left of you and a grill to the right. There is also a street'
                       'in front of you and what looks like a park in the distance.',
        'PATHS': {
            'NORTH': 'LIVING ROOM',
            'SOUTH': 'MAIN STREET'
        }
    },
    'GARAGE': {
        'NAME': 'Garage',
        'DESCRIPTION': 'The garage is small, there is no car inside. There are empty, dusty shelves'
                       ' all across the walls.',
        'PATHS': {
            'NORTH': 'PORCH',
            'SOUTH': 'STREET 2'
        }
    },
    'MAIN STREET': {
        'NAME': 'Street',
        'DESCRIPTION': 'To the south, there is a park and to the east, more street. To the west... more street.',
        'PATHS': {
            'NORTH': 'PORCH',
            'SOUTH': 'PARK',
            'EAST': 'STREET 2',
            'WEST': 'STREET 3'
        }
    },
    'STREET 2': {
        'NAME': 'East Street',
        'DESCRIPTION': 'To the east, it looks like there is a gate to what seems to be a neighborhood, to the west'
                       '... more street.',
        'PATHS': {
            'NORTH': 'GARAGE',
            'EAST': 'NEIGHBORHOOD GATE',
            'WEST': 'MAIN STREET'
        }
    },
    'STREET 3': {
        'NAME': 'West Street',
        'DESCRIPTION': 'To the west... more street. To the east... more street.',
        'PATHS': {
            'EAST': 'STREET',
            'WEST': 'WEST STREET 2'
        }
    },
    'STREET 4': {
        'NAME': 'West Street 2',
        'DESCRIPTION': 'To the east... more street. To the west, it looks like there is a gate to what seems to be'
                       ' a town.',
        'PATHS': {
            'EAST': 'STREET 3',
            'WEST': 'TOWN GATE'
        }
    },
    'TOWN GATE': {
        'NAME': 'Town Gate',
        'DESCRIPTION': 'The gate seems to be locked, with no other way around it. To the east... more street.',
        'PATHS': {
            'EAST': 'WEST STREET 2'
        }
    },
    'NEIGHBORHOOD GATE': {
        'NAME': 'Neighborhood Gate',
        'DESCRIPTION': 'The gate seems to be locked, with no other way around it. To the west... more street.',
        'PATHS': {
            'WEST': 'STREET 2'
        }
    },
    'PARK': {
        'NAME': 'Park Gate',
        'DESCRIPTION': 'The park gate is unlocked, to the north, street. To the south, there is an old playground.',
        'PATHS': {
            'NORTH': 'MAIN STREET',
            'SOUTH': 'PLAYGROUND'
        }
    },
    'PLAYGROUND': {
        'NAME': 'Playground',
        'DESCRIPTION': 'All of the things on the playground seem to be old. To the north, the park gate. To the south'
                       ' a gate to a pond. To the east, a building that says restrooms. To the west, another gated,'
                       'area.',
        'PATHS': {
            'NORTH': 'PARK',
            'SOUTH': 'SOUTH GATED AREA',
            'EAST': 'RESTROOMS',
            'WEST': 'WEST GATED AREA'
        }
    },
    'SOUTH GATED AREA': {
        'NAME': 'South Gated Area',
        'DESCRIPTION': 'The gate to the pond seems to be locked. To the north, the playground.',
        'PATHS': {
            'NORTH': 'PLAYGROUND',
            'SOUTH': 'POND'
        }
    },
    'POND': {
        'NAME': 'Pond',
        'DESCRIPTION': 'There is a pond that is full of algae and the water is really dirty. To the north the '
                       'playground.',
        'PATHS': {
            'NORTH': 'PLAYGROUND'
        }
    },
    'WEST GATED AREA': {
        'NAME': 'West Gated Area',
        'DESCRIPTION': 'The gate seems to be locked, there is not really anything to gate up. To the east, the '
                       'playground',
        'PATHS': {
            'EAST': 'PLAYGROUND'
        }
    },
    'RESTROOMS': {
        'NAME': 'Restrooms',
        'DESCRIPTION': 'There are dirty old restrooms that stink. To the east, the playground.',
        'PATHS': {
            'EAST': 'PLAYGROUND'
        }
    }
}

current_node = world_map['SPAWN']
directions = ['SOUTH', 'NORTH', 'EAST', 'WEST', 'DOWN', 'UP', 'NE', 'NORTHEAST', 'SE', 'SOUTHEAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    elif command == 'JEFF':
        if current_node == world_map['SPAWN']:
            print("Your friend Jeff came out of the closet, said 'mY NamE JeFf', and ate you")
            quit(0)
    else:
        print("Command not recognized")
