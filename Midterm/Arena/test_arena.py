import pytest
import random
from unittest.mock import patch, mock_open

from pokemon import Pokemon
from arena import Arena


@pytest.fixture
def charizard():
    return Pokemon("Charizard")


@pytest.fixture
def squirtle():
    return Pokemon("Squirtle")


@pytest.fixture
def arena(charizard, squirtle):
    arena = Arena()
    arena.add(charizard)
    arena.add(squirtle)
    return arena


def test_arena_add_child_class(arena):
    """An Arena accepts any Pokemon or creature derived from Pokemons"""

    class ChildPokemon(Pokemon):
        pass

    child = ChildPokemon("Test")
    arena.add(child)


def test_arena_add_invalid_type(arena):
    """add raises an exception with an invalid parameter"""
    with pytest.raises(AttributeError):
        arena.add(random.randint(0, 100))

    with pytest.raises(AttributeError):
        arena.add("abcdef")


def test_arena_active(arena, charizard, squirtle):
    """Checks the active method"""
    active = arena.active()
    assert charizard in active
    assert squirtle in active

    squirtle.health = 0
    active = arena.active()
    assert squirtle not in active


def test_arena_len(arena):
    """Checks the length of the arena"""
    assert len(arena) == 2
    other = Pokemon("3rd one")
    arena.add(other)
    assert len(arena) == 3

    other.health = 0
    assert len(arena) == 2


CSV_FILE = """name,health,level
Pikachu,100,1
Charizard,50,2
Squirtle,0,1
"""


@patch("builtins.open", new_callable=mock_open, read_data=CSV_FILE)
def test_load_from_file(mock_file):
    """Checks the load_from_file method using a mocked file (see above)"""
    arena = Arena()
    arena.load_from_file("midterms.txt")
    assert mock_file.call_count == 1
    assert len(arena) == 2

    assert "Pikachu" in [p.name for p in arena.active()]
    assert "Charizard" in [p.name for p in arena.active()]
    assert "Squirtle" not in [p.name for p in arena.active()]
