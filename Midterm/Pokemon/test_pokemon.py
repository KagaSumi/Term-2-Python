import pytest
import inspect
import random
from pokemon import Pokemon


@pytest.fixture
def pikachu():
    """Fixture: a Pokemon instance with predefined attributes"""
    return Pokemon(
        "Pikachu",
        "electric",
    )


def test_pokemon_constructor(pikachu):
    """Check the attributes of the Pokemon"""
    assert pikachu.name == "Pikachu"

    valid = ["fire", "water", "grass", "electric"]
    for element in valid:
        p = Pokemon("Pikachu", element)
        assert p.element == element

    with pytest.raises(ValueError):
        Pokemon("Pikachu", str(random.randint(1000, 9999)))
    with pytest.raises(ValueError):
        Pokemon("Pikachu", random.randint(0, 100))
    with pytest.raises(ValueError):
        Pokemon("Pikachu", [])


def test_pokemon_str(pikachu):
    """string implementation"""
    pikachu.attack = 50
    pikachu.armor = 20
    assert str(pikachu) == "<Pikachu [electric] (100, 50, 20)>"


def test_pokemon_get_attributes(pikachu):
    """Checks additional attributes of the Pokemon"""
    # All Pokemons start at level 1
    assert pikachu.level == 1
    assert pikachu.health == 100

    # And with 0 armor / attack
    assert pikachu.attack == 0
    assert pikachu.armor == 0


def test_pokemon_health(pikachu):
    """Checks the health attribute and the set_health method"""
    # The health for a pokemon is 100 times its level when the Pokemon is created
    assert pikachu.health == 100

    # We can set its health points to any positive integer value...
    pikachu.set_health(50)
    assert pikachu.health == 50

    pikachu.set_health(0)
    assert pikachu.health == 0

    # But we cannot set its value below 0, even if we use a negative number
    # In that case, the health is set to 0

    pikachu.set_health(-100)
    assert pikachu.health == 0


def test_pokemon_invalid_health(pikachu):
    """Checks set_health with an invalid parameter raises an exception"""
    # Using anything else than an integer will raise a ValueError
    invalid = ["abc", "10", [], {"why": "not"}]
    for health in invalid:
        with pytest.raises(ValueError):
            pikachu.set_health(health)


def test_pokemon_level_up(pikachu):
    """Leveling up a Pokemon resets its health"""
    pikachu.level_up()
    assert pikachu.level == 2
    assert pikachu.health == 200

    pikachu.set_health(1)
    pikachu.level_up()
    assert pikachu.level == 3
    assert pikachu.health == 300


def test_pokemon_fight_invalid(pikachu):
    """A Pokemon can only fight another Pokemon"""
    invalid = ["abc", "10", [], {"why": "not"}, random.randint(0, 100)]
    for item in invalid:
        with pytest.raises(ValueError):
            pikachu.fight(item)


def test_pokemon_fight(pikachu):
    """Checks the fight system"""
    # A attacks B
    # damage_B = attack_A - armor_B (or 0)
    # hp_B = hp_B - damage_B
    # damage_A = attack_B - armor_A - attack_A (or 0)
    # hp_A = hp_A - damage_A

    squirtle = Pokemon("Squirtle", "water")
    squirtle.attack = 20
    squirtle.armor = 10

    pikachu.set_health(200)
    pikachu.attack = 50
    pikachu.armor = 0

    # Pikachu: 200, 50, 0
    # Squirtle: 100, 20, 10

    pikachu.fight(squirtle)
    assert pikachu.health == 200
    assert squirtle.health == 60

    squirtle.fight(pikachu)
    assert pikachu.health == 180
    assert squirtle.health == 40


def test_is_active(pikachu):
    """Checks the is_active method"""
    assert pikachu.is_active()
    pikachu.set_health(0)
    assert pikachu.is_active() is False
    pikachu.set_health(-50)
    assert pikachu.is_active() is False
    pikachu.set_health(10)
    assert pikachu.is_active()


def test_docstring_has_answer_to_question():
    """Final question"""
    docstring = inspect.getdoc(Pokemon)
    # Make sure you answer the question asked in the instructions in your docstring!
    assert docstring and "I READ THE TESTS AND INSTRUCTIONS" in docstring
