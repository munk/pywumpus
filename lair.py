from random import randint
from player import Player

def generate_hazard_locations():
    """Create a set of five rooms with hazards"""
    rooms = list(range(1, 20))
    size = 18
    hazards = []
    for _ in range(5):
        choice = randint(0, size)
        size -= 1
        hazards.append(rooms[choice])
        del rooms[choice]

    return hazards
        
class Lair(object):
    def __init__(self):
        self.lair_map = {0: (1, 4, 7), 1: (0, 2, 9), 2: (1, 3, 11), 3: (2, 4, 13),
                         4: (0, 3, 5), 5: (4, 6, 14), 6: (5, 7, 16), 7: (0, 6, 8),
                         8: (7, 9, 17), 9: (1, 8, 10), 10: (9, 11, 18), 11: (2, 10, 12),
                         12: (11, 13, 19), 13: (3, 12, 14), 14: (5, 13, 15), 15: (14, 16, 19),
                         16: (6, 15, 17), 17: (8, 16, 18), 18: (10, 17, 19), 19: (12, 15, 18)}
        bat1, bat2, pit1, pit2, self.wumpus = generate_hazard_locations()
        self.bats = [bat1, bat2]
        self.pits = [pit1, pit2]
        self.player = Player()

    def print(self):
        print("Bats", self.bats)
        print("Pits", self.pits)
        print("Wumpus", self.wumpus)
        print("Player", self.player.location)

    def get_player_move_choices(self):
        return list(self.lair_map[self.player.location])

    def get_arrow_path(self, start, expected_path):
        if len(expected_path) > 5:
            expected_path = expected_path[:5]
        neighbors = self.lair_map[start] 
        actual_path = []
        for p in expected_path:
            if p in neighbors:
                actual_path.append(p)
                neighbors = self.lair_map[p]
            else:
                q = neighbors[randint(0, 2)]
                actual_path.append(q)
                neighbors = self.lair_map[q]
        return actual_path

    def shoot_arrow(self, expected_path): #TODO: move this to player
        start = self.player.location
        self.player.ammo -= 1
        path = self.get_arrow_path(start, expected_path)
        print(path)
        for p in path:
            if p == self.player.location:
                raise Exception("You were hit by an arrow!")
            if p == self.wumpus:
                raise Exception("You killed the Wumpus!")

    def check_nearby_hazards(self):
        loc = self.player.location
        neighbors = self.lair_map[loc]
        message = ''
        for n in neighbors:
            if n in self.bats:
                text = " You hear bats nearby. "
            elif n in self.pits:
                text = " You feel a draft. "
            elif n == self.wumpus:
                text = " You smell a Wumpus! "
            else:
                text = ""

            if text not in message:
                message += text
        return message
            

    def move_player(self, choice):
        current_location = self.lair_map[self.player.location]
        self.player.location = current_location[choice]

        if self.player.location in self.pits:
            raise Exception("You fell down a pit")

        if self.player.location == self.wumpus:
            #TODO: Allow the wumpus a chance to move
            raise Exception("The wumpus ate you")
        
        if self.player.location in self.bats:
            self.player.location = randint(0, 19)
            print("Bats have snatched you and moved you to another room!")

        message = self.check_nearby_hazards()
        return message
            
