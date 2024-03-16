import pytest
from die import Die


def test_has_value_attribute():
    assert hasattr(Die(), 'value')

def test_value_initialised_to_none():
    assert Die().value is None

def test_value_cannot_be_changed_outside_the_class():
    with pytest.raises(AttributeError):
        Die().value = 10
