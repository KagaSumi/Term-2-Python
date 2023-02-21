class Bakery:
    def __init__(self, name):
        self.name = name
        self.croissants = 0
        self.money = 0

    def bake(self, number):
        self.croissants += helper(number)

    def sell(self, number=1):
        number = helper_2(number)
        if self.croissants < number:
            raise RuntimeError
        self.croissants -= number
        self.money += number*3

    def __str__(self):
        return self.name


def helper(number):
    if isinstance(number, float):
        raise ValueError
    if isinstance(number, str):
        try:
            number = int(number)
        except TypeError:
            raise AttributeError
    if number < 0:
        raise ValueError
    return number


def helper_2(number):
    if isinstance(number, float):
        raise ValueError
    if isinstance(number, str):
        raise ValueError
    if number < 0:
        raise ValueError
    return number
