import pytest
from plates import find_next_plate, check_plate


def test_check_plate():
    """The correct format is: NN-LL-NN, where:
    N is a number from 1 to 9
    L is an uppercase letter (from A to Z)"""

    invalid_plates = [
        "A",
        "AA-11-AA",
        "1A-AA-11",
        "11-AA-1A",
        "11-A1-11",
        "00-AA-00",
        "11-a1-11",
    ]
    for plate in invalid_plates:
        assert not check_plate(plate)


def test_find_next_by_one():
    """Basic increments"""
    result = find_next_plate("11-AA-11")
    assert result == "11-AA-12"

    result = find_next_plate("11-AA-19")
    assert result == "11-AA-21"

    result = find_next_plate("11-AA-99")
    assert result == "11-AB-11"

    result = find_next_plate("11-AZ-99")
    assert result == "11-BA-11"

    result = find_next_plate("11-ZZ-99")
    assert result == "12-AA-11"


def test_find_next():
    """Increments, with an argument"""
    result = find_next_plate("11-AA-11", 1)
    assert result == "11-AA-12"

    result = find_next_plate("11-AA-11", 8)
    assert result == "11-AA-19"

    result = find_next_plate("11-AA-11", 81)
    assert result == "11-AB-11"

    result = find_next_plate("11-BZ-11", 81)
    assert result == "11-CA-11"

    result = find_next_plate("15-ZZ-12", 80)
    assert result == "16-AA-11"


def test_find_next_impossible():
    """Impossible plate requests should raise an OverFlow exception"""
    with pytest.raises(OverflowError):
        find_next_plate("99-ZZ-99")

    with pytest.raises(OverflowError):
        find_next_plate("99-ZZ-98", 2)
