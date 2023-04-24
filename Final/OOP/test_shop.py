from shop import Shop


def test_constructor_location():
    burnaby = Shop("burnaby")
    assert burnaby.location == "burnaby"


def test_constructor_inventory():
    vancouver = Shop("Vancouver")
    assert vancouver.get_inventory() == {}


def test_add_product():
    vancouver = Shop("Vancouver")
    vancouver.add_product("skis", 10)
    vancouver.add_product("snowboard", 5)

    inventory = vancouver.get_inventory()

    assert inventory["skis"] == 10
    assert inventory["snowboard"] == 5

    vancouver.add_product("skis", 20)
    inventory = vancouver.get_inventory()
    assert inventory["skis"] == 20


def test_len():
    vancouver = Shop("Vancouver")
    assert len(vancouver) == 0

    vancouver.add_product("skis", 10)
    vancouver.add_product("snowboard", 5)

    assert len(vancouver) == 2


def test_str():
    vancouver = Shop("Vancouver")
    vancouver.add_product("skis", 10)
    vancouver.add_product("snowboard", 5)

    assert str(vancouver) == "<Store: Vancouver (2 products)>"
