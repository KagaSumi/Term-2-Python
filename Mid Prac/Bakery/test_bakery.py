import pytest
from bakery import Bakery


@pytest.fixture
def bakery():
    """Your local neighbourhood bakery. Tasty croissants!"""
    return Bakery("Tim's bakery")


def test_attributes(bakery):
    """Test the attributes of the instance. Uses the fixture above."""
    assert bakery.name == "Tim's bakery"
    assert bakery.croissants == 0
    assert bakery.money == 0


def test_bake(bakery):
    """
    Test the bake method. The total number of croissants increases.
    The method takes any kind of argument that can be converted to an integer.
    """

    bakery.bake(100)
    assert bakery.croissants == 100

    bakery.bake("100")
    assert bakery.croissants == 200


def test_bake_invalid_params(bakery):
    """Test the argument to bake can only be "similar" to a positive integer"""

    bakery.bake("100")

    with pytest.raises(ValueError):
        bakery.bake(1.5)

    with pytest.raises(ValueError):
        bakery.bake(-100)

    with pytest.raises(ValueError):
        bakery.bake("abc")


def test_sell(bakery):
    """
    Test the sell method. The default behaviour is to sell 1 croissant.
    A croissant costs $3.
    """

    bakery.bake(100)
    bakery.sell()
    assert bakery.croissants == 99
    assert bakery.money == 3

    bakery.sell(10)
    assert bakery.croissants == 89
    assert bakery.money == 33


def test_sell_invalid_params(bakery):
    """The number to sell can only be a positive integer"""
    with pytest.raises(ValueError):
        bakery.sell(1.5)

    with pytest.raises(ValueError):
        bakery.sell("10")

    with pytest.raises(ValueError):
        bakery.sell(-100)

    with pytest.raises(ValueError):
        bakery.sell("100")

    with pytest.raises(ValueError):
        bakery.sell("abc")


def test_sell_more_than_available(bakery):
    """Test that you can not sell more croissants than available"""
    bakery.bake(10)
    bakery.sell(5)

    with pytest.raises(RuntimeError):
        bakery.sell(100)


def test_str(bakery):
    """Dunder method"""
    assert str(bakery) == "Tim's bakery"
