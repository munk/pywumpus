import lair

def test_generate_hazard_locations():
    locs = lair.generate_hazard_locations()
    assert len(locs) == 5
    assert all(map(lambda i: isinstance(i, int), locs))

def test_generate_hazard_locations_no_dups():
    locs = lair.generate_hazard_locations()
    assert len(set(locs)) == 5

def test_move_player():
    l = lair.Lair()
    try:
        l.move_player(2)
    except:
        pass # Ignore game loosing conditions
    assert l.player.location == 7, l.player.location

def test_get_arrow_path():
    l = lair.Lair()
    start = 0
    arrow_path = [1, 2, 3, 4, 5]
    assert l.get_arrow_path(start, arrow_path) == arrow_path
    
def test_get_arrow_path_not_more_than_five():
    l = lair.Lair()
    start = 0
    arrow_path = [1, 2, 3, 4, 5, 7]
    assert len(l.get_arrow_path(start, arrow_path)) == 5

def test_get_arrow_path():
    l = lair.Lair()
    start = 0
    arrow_path = [1, 2, 3, 4, 19]
    assert l.get_arrow_path(start, arrow_path) != arrow_path

def test_shoot_arrow():
    l = lair.Lair()
    ammo = l.player.ammo
    l.shoot_arrow( [])
    assert ammo - 1 == l.player.ammo

def test_shoot_arrow_is_safe():
    l = lair.Lair()
    try:
        l.shoot_arrow( [1])
    except Exception as e:
        assert e.args[0] != "You were hit by an arrow!"

def test_shoot_arrow_kills_player():
    l = lair.Lair()
    try:
        l.shoot_arrow( [1, 0])
    except Exception as e:
        assert e.args[0] == "You were hit by an arrow!"
        return
    assert False, "Exception expected but not caught"

def test_shoot_arrow_kills_wumpus():
    l = lair.Lair()
    l.wumpus = 1
    try:
        l.shoot_arrow( [1, 0])
    except Exception as e:
        assert e.args[0] == "You killed the Wumpus!"
        return
    assert False, "Exception expected but not caught"

def test_pit_ends_game():
    pass #TODO: Implememnt me

def test_bat_moves_player():
    pass #TODO: Implement me

def test_check_nearby_hazards():
    l = lair.Lair()
    l.bats = [1, 4]
    l.wumpus = 14
    assert l.check_nearby_hazards() == " You hear bats nearby. ", l.check_nearby_hazards()

    l.bats = [5, 6]
    l.pits = [1, 4]
    l.wumpus = 14
    assert l.check_nearby_hazards() == " You feel a draft. ", l.check_nearby_hazards()

    l.bats = [5, 6]
    l.pits = [9, 10]
    l.wumpus = 1
    assert l.check_nearby_hazards() == " You smell a Wumpus! ", l.check_nearby_hazards()

def test_generate_hazard_locations_edgecase():
    f = lair.randint
    lair.randint = lambda x, y: y
    try:
        lair.generate_hazard_locations()
    except IndexError:
        assert False
    finally:
        lair.randint = f

