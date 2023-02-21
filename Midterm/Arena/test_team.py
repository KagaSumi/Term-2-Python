import pytest

from pokemon import Pokemon
from arena import Arena, Team


@pytest.fixture
def charizard():
    charizard = Pokemon("Charizard")
    charizard.level = 2
    return charizard


@pytest.fixture
def squirtle():
    return Pokemon("Squirtle")


@pytest.fixture
def arena(charizard, squirtle):
    arena = Arena()
    arena.add(charizard)
    arena.add(squirtle)
    return arena


def test_make_team(arena):
    """Checks the type of the return value for make_team"""
    team = arena.make_team(1)
    assert type(team) is Team
    assert not isinstance(team, Arena)


def test_make_team_level(arena, squirtle, charizard):
    """Checks the make_team and get_pokemons methods"""

    # Level 1 team - only Squirtle
    team = arena.make_team(1)
    assert squirtle in team.get_pokemons()

    # Level 2 team - only Charizard
    team = arena.make_team(2)
    assert charizard in team.get_pokemons()

    charizard.health = 0
    team = arena.make_team(2)
    assert team.get_pokemons() == []

    # Level 3 team - no pokemons!
    team = arena.make_team(3)
    assert team.get_pokemons() == []
