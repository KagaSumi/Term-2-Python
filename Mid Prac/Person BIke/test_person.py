import pytest
from person import Person

def test_person_valid_parameters():
    p = Person("Tim", 20)
    assert p.name == "Tim"
    assert p.age == 20

def test_person_invalid_name():
    with pytest.raises(AttributeError):
        Person(12345, 20)

    with pytest.raises(AttributeError):
        Person("AB", 20)

def test_person_invalid_age():
    with pytest.raises(AttributeError):
        Person("Tim", -1)

def test_person_get_name():
    p = Person("Tim", 20)
    assert p.get_name() == "TIM / 20"

    p = Person("John Wick", 40)
    assert p.get_name() == "JOHN WICK / 40"