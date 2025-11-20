import random
from  Pokemon import *
from pessoa import Inimigo
from Pokemon import *

def explorar():
    evento = random.randint(1, 3)
    if evento == 1:
        print("Um treinador apareceu!")
        return Inimigo()
    elif evento == 2:
        print("Um Pokémon selvagem apareceu!")
        return Inimigo()
    else:
        print("Nada aconteceu.")
        return None
