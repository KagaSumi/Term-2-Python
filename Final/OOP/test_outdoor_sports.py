from unittest.mock import patch

import pytest

from bcit_sports import OutdoorShop
from shop import Shop


class Response404:
    status_code = 404

    def json(self):
        return "The mock has no JSON."


class ResponseOK:
    status_code = 200

    def json(self):
        return {"products": {"tent": 25, "kayak": 5, "snowboard": 10}}


def test_class_relationship():
    vancouver = OutdoorShop("vancouver")
    assert isinstance(vancouver, Shop)


@patch("requests.get")
def test_load_404(mock_get):
    mock_get.return_value = Response404()
    vancouver = OutdoorShop("vancouver")
    with pytest.raises(UserWarning):
        vancouver.load()
    assert mock_get.call_count == 1
    assert "bcitoutdoor.ca/api/store/vancouver" in mock_get.call_args[0][0]
    assert vancouver.get_inventory() == {}


@patch("requests.get")
def test_load_ok(mock_get):
    mock_get.return_value = ResponseOK()
    vancouver = OutdoorShop("vancouver")
    vancouver.load()
    assert mock_get.call_count == 1
    assert "bcitoutdoor.ca/api/store/vancouver" in mock_get.call_args[0][0]
    assert vancouver.get_inventory() == {
        "tent": 25,
        "snowboard": 10,
        "kayak": 5,
    }
