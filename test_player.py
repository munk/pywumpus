from player import Player

def test_create_player():
    p = Player()
    assert p.ammo == 5
    assert p.location == 0
