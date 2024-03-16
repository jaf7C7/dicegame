from player import Player


def test_has_die_attribute():
    assert hasattr(Player(), 'die')

def test_die_attribute_is_die_instance():
    from die import Die
    assert isinstance(Player().die, Die)

def test_has_is_cpu_attribute():
    assert hasattr(Player(), 'is_cpu')

def test_is_cpu_attr_is_boolean():
    assert isinstance(Player().is_cpu, bool)
