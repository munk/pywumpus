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
    l.move_player(2)
    assert l.player.location == 7, l.player.location
    
def test_generate_hazard_locations_edgecase():
    f = lair.randint
    lair.randint = lambda x, y: y
    try:
        lair.generate_hazard_locations()
    except IndexError:
        assert False
    finally:
        lair.randint = f

