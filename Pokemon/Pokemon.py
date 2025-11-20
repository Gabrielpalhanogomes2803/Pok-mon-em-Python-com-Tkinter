import random

class Pokemon:
    def __init__(self, nome, level=1):
        self.nome = nome
        self.level = level
        self.hp = level * 10

    def __str__(self):
        return f"{self.nome} (Lv {self.level})"

    def atacar(self, outro):
        dano = random.randint(1, 5) + self.level
        outro.hp -= dano
        if outro.hp < 0:
            outro.hp = 0
        return dano

    def aumentar_level(self):
        # A cada 3 vitórias do player, o pokemon aumenta level
        self.level += 1
        self.hp = self.level * 10

class PokemonEletrico(Pokemon):
    pass

class PokemonDeFogo(Pokemon):
    pass

class PokemonDeAgua(Pokemon):
    pass


