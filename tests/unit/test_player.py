import pytest
from player import Player


class TestDie:
    def test_has_die_attribute(self):
        assert hasattr(Player(), 'die')

    def test_die_attribute_is_die_instance(self):
        from die import Die
        assert isinstance(Player().die, Die)

    def test_die_is_protected_attribute(self):
        with pytest.raises(AttributeError):
            Player().die = 'new die'


class TestIsCPU:
    def test_has_is_cpu_attribute(self):
        assert hasattr(Player(), 'is_cpu')

    def test_is_cpu_attr_is_boolean(self):
        assert isinstance(Player().is_cpu, bool)


class TestCounter:
    def test_has_counter_attribute(self):
        assert hasattr(Player(), 'counter')

    def test_counter_initialised_to_10(self):
        assert Player().counter == 10
