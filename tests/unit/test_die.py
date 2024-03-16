from die import Die


def test_has_value_attribute():
    assert hasattr(Die(), 'value')

def test_value_initialised_to_none():
    assert Die().value is None
