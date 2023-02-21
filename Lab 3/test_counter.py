import pytest

from counter import Countdown

def test_counter_init():
    c = Countdown(start=100, step=1)
    assert c.current == 100
    assert c.step == 1
    assert c.complete is False

def test_counter_down():
    c = Countdown(start=100, step=1)
    for x in range(100):
        c.down()

    assert c.current == 0
    assert c.complete is True

def test_counter_down_step2():
    c = Countdown(start=100, step=2)
    c.down()
    assert c.current == 98
    assert c.complete is False

    for x in range(100):
        c.down()

    assert c.complete is True
