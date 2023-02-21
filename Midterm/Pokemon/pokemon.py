class Pokemon:
    """
    A couple of things to improve this class is to add more types, and have the damage modifiers associated with classes implemented here
    and not all pokemon grow is the same rate in each stat so have some global modifiers to their indivisual stat growth rates
    I READ THE TESTS AND INSTRUCTIONS
    """

    def __init__(self, name: str, element: str):
        valid_type = ['water', 'fire', 'grass', 'electric']
        if not isinstance(element, str):
            raise ValueError
        if element.lower() not in valid_type:
            raise ValueError
        self.name = name
        self.health = 100
        self.attack = 0
        self.armor = 0
        self.level = 1
        self.element = element.lower()

    def __str__(self):
        return f'<{self.name} [{self.element}] ({self.health}, {self.attack}, {self.armor})>'

    def level_up(self):
        self.level += 1
        self.health = 100 * self.level

    def set_health(self, health: int):
        if not isinstance(health, int):
            raise ValueError
        if health < 0:
            health = 0
        self.health = health

    def is_active(self):
        return self.health > 0

    def fight(self, pokemon_B):
        if not isinstance(pokemon_B, Pokemon):
            raise ValueError
        out_damage = self.attack - pokemon_B.armor
        in_damage = pokemon_B.attack - self.armor - self.attack
        if out_damage < 0:
            out_damage = 0
        if in_damage < 0:
            in_damage = 0
        pokemon_B.health -= out_damage
        self.health -= in_damage
