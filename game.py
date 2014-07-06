import lair

if __name__ == '__main__':
    wumpus_home = lair.Lair()

    while True:
        choices = wumpus_home.get_player_move_choices()
        
        for i in range(3):
            print(str(i) + ":", choices[i])
        selection = int(input('Choose a room to move to > '))
        
        wumpus_home.move_player(selection)

