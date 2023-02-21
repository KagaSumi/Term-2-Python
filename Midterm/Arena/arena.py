from csv import reader as read
from pokemon import Pokemon


class Arena:
    def __init__(self):
        self.play_area = []

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = [line for line in read(file)][1:]
        for poke in data:
            new_pokemon = Pokemon(poke[0])
            new_pokemon.health = poke[1]
            new_pokemon.level = poke[2]
            self.play_area.append(new_pokemon)

    def add(self, pokemon: Pokemon):
        if not isinstance(pokemon, Pokemon):
            raise AttributeError
        self.play_area.append(pokemon)

    def __len__(self):
        return len(self.active())

    def active(self):
        active_pokemon = []
        for pokemon in self.play_area:
            if int(pokemon.health) > 0:
                active_pokemon.append(pokemon)
        return active_pokemon

    def make_team(self, level: int):
        valid_pokemon = []
        for pokemon in self.play_area:
            if int(pokemon.level) == level:
                valid_pokemon.append(pokemon)
        return Team(valid_pokemon)


class Team:
    def __init__(self, pokemon=None):
        if pokemon == None:
            self.team = []
        self.team = pokemon

    def get_pokemons(self):
        return list(filter(lambda pokemon: pokemon.health > 0, self.team))


def main():
    temp_arena = Arena()
    temp_arena.load_from_file("pokemons.txt")
    print(temp_arena.play_area)


if __name__ == "__main__":

    main()
