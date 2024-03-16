import pytest
from die import Die


def test_has_value_attribute():
    assert hasattr(Die(), 'value')

def test_value_initialised_to_none():
    assert Die().value is None

def test_value_cannot_be_changed_outside_the_class():
    with pytest.raises(AttributeError):
        Die().value = 10

def test_has_roll_method():
    assert hasattr(Die(), 'roll')

def test_roll_generates_random_numbers_between_1_and_6():
    die = Die()
    for i in range(2):
        die.roll()
        assert die.value in range(1, 7)
