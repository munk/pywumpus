from room import Room

def test_rooms_have_ids():
    r = Room(1, False, True)
    assert r.id_ == 1
    assert r.has_bat == False
    assert r.has_pit == True
