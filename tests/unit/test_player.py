import pytest
from unittest.mock import Mock
from player import Player


class TestDie:

    def test_has_die_attribute(self):
        assert hasattr(Player(), 'die')

    def test_die_is_protected_attribute(self):
        with pytest.raises(AttributeError):
            Player().die = 'new die'

    def test_has_roll_attribute(self):
        assert hasattr(Player(), 'roll_die')

    def test_roll_die_calls_roll_method_on_die_object(self):
        player = Player(die=Mock())
        player.roll_die()
        player.die.roll.assert_called()


class TestIsCPU:

    def test_has_is_cpu_attribute(self):
        assert hasattr(Player(), 'is_cpu')

    def test_is_cpu_attr_is_boolean(self):
        assert isinstance(Player().is_cpu, bool)


class TestCounter:

    def test_has_counter_attribute(self):
        assert hasattr(Player(), 'counter')

    def test_counter_initialised_to_5(self):
        assert Player().counter == 5

    def test_counter_is_a_protected_attribute(self):
        with pytest.raises(AttributeError):
            Player().counter = 0

    def test_has_increment_counter_attribute(self):
        assert hasattr(Player(), 'increment_counter')

    def test_increment_counter_adds_one_to_counter(self):
        player = Player()
        initial = player.counter
        player.increment_counter()
        assert player.counter == initial + 1

    def test_has_decrement_counter_attribute(self):
        assert hasattr(Player(), 'decrement_counter')

    def test_decrement_counter_removes_one_from_counter(self):
        player = Player()
        initial = player.counter
        player.decrement_counter()
        assert player.counter == initial - 1
