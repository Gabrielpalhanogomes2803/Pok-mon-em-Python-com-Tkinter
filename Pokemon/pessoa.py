import random
from Pokemon import *

class Pessoa:
    nomes = ["Gabriel", "Arthur", "Miguel", "Lucas", "Rafael", "Ana", "Julia", "Carolina"]

    def __init__(self, nome=None, pokemons=None):
        self.nome = nome if nome else random.choice(self.nomes)
        self.pokemons = pokemons if pokemons else []

    def __str__(self):
        return self.nome

class Player(Pessoa):
    def __init__(self, nome=None, pokemons=None):
        super().__init__(nome, pokemons)
        self.nivel = 1
        self.vitorias = 0

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self.nome} capturou {pokemon}!")

    def aumentar_vitorias(self):
        self.vitorias += 1
        if self.vitorias % 3 == 0:
            self.nivel += 1
            print(f"{self.nome} subiu para o nível {self.nivel}!")
        # Aumenta level de todos os pokemons do player
        for p in self.pokemons:
            p.aumentar_level()

class Inimigo(Pessoa):
    def __init__(self, player_level=1):
        super().__init__()
        self.pokemons = [self.gerar_pokemon_aleatorio(player_level)]

    def gerar_pokemon_aleatorio(self, level):
        tipos = [PokemonEletrico, PokemonDeFogo, PokemonDeAgua]
        especies = ["Pikachu", "Charmander", "Squirtle"]
        Tipo = random.choice(tipos)
        especie = random.choice(especies)
        return Tipo(especie, level)

