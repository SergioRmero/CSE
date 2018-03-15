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
        'DESCRIPTION': 'none yet',
        'PATHS': {
            'UP': 'ATTIC',
            'SOUTH': 'RESTROOM',
            'WEST': 'BED ROOM 2',
            'NORTH': 'KITCHEN'
        }
    },
    'BED ROOM 2': {
        'NAME': 'Bed Room 2',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'EAST': 'BED ROOM'
        }
    },
    'RESTROOM': {
        'NAME': 'Restroom',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'SOUTH': 'BED ROOM'
        }
    },
    'ATTIC': {
        'NAME': 'Attic',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'DOWN': 'BED ROOM'
        }
    },
    'FRONT DOOR': {
        'NAME': 'Front Door',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'LIVING ROOM',
            'SOUTH': 'PORCH'
        }
    },
    'PORCH': {
        'NAME': 'Porch',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'LIVING ROOM',
            'SOUTH': 'MAIN STREET'
        }
    },
    'GARAGE': {
        'NAME': 'Garage',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'PORCH',
            'SOUTH': 'STREET 2'
        }
    },
    'MAIN STREET': {
        'NAME': 'Street',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'PORCH',
            'SOUTH': 'PARK',
            'EAST': 'STREET 2',
            'WEST': 'STREET 3'
        }
    },
    'STREET 2': {
        'NAME': 'East Street',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'GARAGE',
            'EAST': 'NEIGHBORHOOD GATE',
            'WEST': 'MAIN STREET'
        }
    },
    'STREET 3': {
        'NAME': 'West Street',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'EAST': 'STREET',
            'WEST': 'WEST STREET 2'
        }
    },
    'STREET 4': {
        'NAME': 'West Street 2',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'EAST': 'STREET 3',
            'WEST': 'TOWN GATE'
        }
    },
    'TOWN GATE': {
        'NAME': 'Town Gate',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'EAST': 'WEST STREET 2'
        }
    },
    'NEIGHBORHOOD GATE': {
        'NAME': 'Neighborhood Gate',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'WEST': 'STREET 2'
        }
    },
    'PARK': {
        'NAME': 'Park Gate',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'MAIN STREET',
            'SOUTH': 'PLAYGROUND'
        }
    },
    'PLAYGROUND': {
        'NAME': 'Playground',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'PARK',
            'SOUTH': 'SOUTH GATED AREA',
            'EAST': 'RESTROOMS',
            'WEST': ' WEST GATED AREA'
        }
    },
    'SOUTH GATED AREA': {
        'NAME': 'South Gated Area',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'PLAYGROUND',
            'SOUTH': 'POND'
        }
    },
    'POND': {
        'NAME': 'Pond',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'NORTH': 'PLAYGROUND'
        }
    },
    'WEST GATED AREA': {
        'NAME': 'West Gated Area',
        'DESCRIPTION': 'NONE YET',
        'PATHS': {
            'EAST': 'PLAYGROUND'
        }
    },
    'RESTROOMS': {
        'NAME': 'Restrooms',
        'DESCRIPTION': 'NONE YET',
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
