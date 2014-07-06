import lair

if __name__ == '__main__':
    wumpus_home = lair.Lair()

    while True:
        print(wumpus_home.check_nearby_hazards())
        #wumpus_home.print()

        choices = wumpus_home.get_player_move_choices()
        choices.append("shoot")
        
        for i in range(4):
            print(str(i) + ":", choices[i])
        selection = int(input('Choose a room to move to or to shoot > '))

        if selection == 3:
            selection = list(map(int, input("Enter a list of rooms separated by commas. > ").split(',')))
            print(selection)
            wumpus_home.shoot_arrow(selection)
        else:
            wumpus_home.move_player(selection)

