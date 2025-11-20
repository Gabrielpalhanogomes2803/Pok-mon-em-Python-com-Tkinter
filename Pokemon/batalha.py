import random

def batalha(pokemon_player, pokemon_inimigo):
    pokemon_player.hp = pokemon_player.level * 10
    pokemon_inimigo.hp = pokemon_inimigo.level * 10

    print(f"\n{pokemon_player} VS {pokemon_inimigo}\n")

    while True:
        # Player ataca
        dano = pokemon_player.atacar(pokemon_inimigo)
        # Chance de golpe especial
        if random.randint(1,5) == 1:
            dano_extra = pokemon_player.atacar(pokemon_inimigo)
            print(f"Golpe especial! {pokemon_player} causou {dano_extra} de dano extra!")
            dano += dano_extra

        print(f"{pokemon_player} causou {dano} de dano! HP inimigo: {pokemon_inimigo.hp}/{pokemon_inimigo.level*10}")

        if pokemon_inimigo.hp <= 0:
            print(f"{pokemon_inimigo} desmaiou! Vitória!\n")
            return "win"

        # Inimigo ataca
        dano_inimigo = pokemon_inimigo.atacar(pokemon_player)
        print(f"{pokemon_inimigo} causou {dano_inimigo} de dano! HP player: {pokemon_player.hp}/{pokemon_player.level*10}")

        if pokemon_player.hp <= 0:
            print(f"{pokemon_player} desmaiou! Derrota!\n")
            return "lose"

