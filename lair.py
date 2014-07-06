from random import randint

lair = {0: (1, 4, 7), 
        1: (0, 2, 9), 
        2: (1, 3, 11), 
        3: (2, 4, 13),
        4: (0, 3, 5), 
        5: (4, 6, 14), 
        6: (5, 7, 16), 
        7: (0, 6, 8),
        8: (7, 9, 17), 
        9: (1, 8, 10), 
        10: (9, 11, 18), 
        11: (2, 10, 12),
        12: (11, 13, 19), 
        13: (3, 12, 14), 
        14: (5, 13, 15), 
        15: (14, 16, 19),
        16: (6, 15, 17), 
        17: (8, 16, 18), 
        18: (10, 17, 19),
        19: (12, 15, 18)}

def generate_hazard_locations():
    rooms = list(range(0, 20))
    size = 19
    hazards = []
    for _ in range(5):
        choice = randint(0, size)
        size -= 1
        hazards.append(rooms[choice])
        del rooms[choice]

    return hazards
        
