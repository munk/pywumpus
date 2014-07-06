class Room(object):
    def __init__(self, id, has_bat=False, has_pit=False):
        self.id_ = id 
        self.has_bat = has_bat
        self.has_pit = has_pit
