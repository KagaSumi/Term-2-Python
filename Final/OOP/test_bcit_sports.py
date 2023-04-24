from unittest.mock import mock_open, patch

import pytest

from bcit_sports import BCITSports, EastCoastShop, OutdoorShop
from shop import Shop

CSV_DATA_1 = """item,quantity
tent,10
hockey puck,50
kayak,5
"""


class Response404:
    status_code = 404

    def json(self):
        return "The mock has no JSON."


class ResponseOK:
    status_code = 200

    def json(self):
        return {"products": {"tent": 25, "kayak": 5, "snowboard": 15}}


def test_inheritance():
    """BCIT Sports is not a shop"""
    all = BCITSports()
    assert not isinstance(all, (Shop, OutdoorShop, EastCoastShop))


@patch("requests.get")
def test_where_api(mock_get):
    """API returns information"""
    all = BCITSports()

    mock_get.return_value = ResponseOK()
    with patch("builtins.open", side_effect=FileNotFoundError) as mock_file:
        registered = all.register_store("langley")
        assert mock_file.call_count == 0
    assert registered is True
    assert "kayak" in all.products()
    assert "tent" in all.products()
    assert "snowboard" in all.products()
    assert all.where("kayak") == ["langley"]


@patch("requests.get")
def test_where_api_404(mock_get):
    """API does not have information, file does not have information"""
    all = BCITSports()

    mock_get.return_value = Response404()
    with patch("builtins.open", side_effect=FileNotFoundError) as mock_file:
        registered = all.register_store("langley")
        assert mock_file.call_count == 1
    assert registered is False
    assert all.products() == []


@patch("requests.get")
def test_where_api_404_file(mock_get):
    """API does not have information, file does"""
    all = BCITSports()

    mock_get.return_value = Response404()
    with patch(
        "builtins.open", new_callable=mock_open, read_data=CSV_DATA_1
    ) as mock_file:
        registered = all.register_store("burnaby")
        assert mock_file.call_count == 1
    assert registered is True
    assert "kayak" in all.products()
    assert "hockey puck" in all.products()
    assert "tent" in all.products()
    assert all.where("kayak") == ["burnaby"]


@pytest.fixture
@patch("requests.get")
def two_shops(mock_get):
    """Fixture with 2 shops preloaded: Burnaby (API) and Toronto (file)"""
    all = BCITSports()

    mock_get.return_value = ResponseOK()
    with patch("builtins.open", side_effect=FileNotFoundError):
        all.register_store("burnaby")

    mock_get.return_value = Response404()
    with patch("builtins.open", new_callable=mock_open, read_data=CSV_DATA_1):
        all.register_store("toronto")

    return all


def test_products(two_shops):
    assert "kayak" in two_shops.products()
    assert "tent" in two_shops.products()
    assert "hockey puck" in two_shops.products()


def test_where_multiple(two_shops):
    assert two_shops.where("edamame") == []
    assert "burnaby" in two_shops.where("kayak")
    assert "toronto" in two_shops.where("kayak")

    assert "toronto" not in two_shops.where("snowboard")
    assert "burnaby" not in two_shops.where("hockey puck")


def test_available(two_shops):
    assert two_shops.available("edamame") == 0
    assert two_shops.available("kayak") == 10
    assert two_shops.available("snowboard") == 15
    assert two_shops.available("hockey puck") == 50
