class Bike:
    def __init__(self):
        self.rider = None
        self.distance = 0

    def start_rental(self, rider):
        if self.rider is not None:
            raise RuntimeError
        self.rider = rider

    def bike(self, travel):
        if travel < 0:
            raise AttributeError
        if self.rider is None:
            raise RuntimeError
        self.distance += travel

    def end_rental(self):
        if self.rider is None:
            raise RuntimeError
        store_distance = self.distance
        self.rider = None
        self.distance = 0
        return store_distance
