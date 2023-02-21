import pytest
from bike import Bike

def test_bike():
    """The Car class takes NO arguments"""
    bike = Bike()
    assert bike.rider is None
    assert bike.distance == 0

def test_bike_no_arguments():
    """The Car class takes NO arguments"""
    with pytest.raises(TypeError):
        Bike(None, 0)

def test_bike_cannot_bike_without_rider():
    """The bike must have a rider before it can be used"""
    bike = Bike()
    with pytest.raises(RuntimeError):
        bike.bike(100)

def test_bike_start_rental():
    """
    When the rental begins, the name of the biker is set.
    There can only be one rental at a time.
    """

    bike = Bike()
    bike.start_rental("Tim")
    assert bike.rider == "Tim"

    with pytest.raises(RuntimeError):
        bike.start_rental("Other biker")

def test_bike_bike():
    """The bike method keeps track of the distance ridden"""
    bike = Bike()
    bike.start_rental("Tim")
    assert bike.distance == 0
    bike.bike(100)
    assert bike.distance == 100
    bike.bike(200)
    assert bike.distance == 300

    with pytest.raises(AttributeError):
        bike.bike(-500)

    assert bike.distance == 300

def test_bike_end_rental():
    """
    end_rental terminates the rental, and RETURNS the distance driven
    rider and distance are reset to their default values (None, 0)
    """

    bike = Bike()
    with pytest.raises(RuntimeError):
        bike.end_rental()

    bike.start_rental("Tim")
    bike.bike(500)
    distance = bike.end_rental()
    assert distance == 500
    assert bike.distance == 0
    assert bike.rider is None