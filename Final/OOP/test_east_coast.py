from unittest.mock import mock_open, patch

import pytest

from bcit_sports import EastCoastShop
from shop import Shop

CSV_DATA = """item,quantity
tent,10
hockey puck,50
kayak,5
"""


def test_class_relationship():
    toronto = EastCoastShop("toronto")
    assert isinstance(toronto, Shop)


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_not_found(mock_file):
    toronto = EastCoastShop("toronto")
    with pytest.raises(UserWarning):
        toronto.load()
    assert mock_file.call_count == 1
    assert "stores/toronto.txt" in mock_file.call_args[0][0]
    assert toronto.get_inventory() == {}


@patch("builtins.open", new_callable=mock_open, read_data=CSV_DATA)
def test_load_ok(mock_file):
    toronto = EastCoastShop("ottawa")
    toronto.load()
    assert mock_file.call_count == 1
    assert "stores/ottawa.txt" in mock_file.call_args[0][0]
    assert toronto.get_inventory() == {
        "tent": 10,
        "hockey puck": 50,
        "kayak": 5,
    }
