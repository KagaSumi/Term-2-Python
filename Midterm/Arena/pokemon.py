class Pokemon:
    def __init__(self, name):
        """Initializes the attributes of the class"""
        self.name = name
        self.health = 100
        self.level = 1

    def join(self, arena):
        """Makes the Pokemon join the arena provided"""
        arena.add(self)
