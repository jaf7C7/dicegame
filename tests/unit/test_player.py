from player import Player


def test_has_die_attribute():
    assert hasattr(Player(), 'die')
