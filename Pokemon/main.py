import tkinter as tk
from gui import PokemonGUI
from pessoa import Player
from save_load import carregar_jogo

def main():
    root = tk.Tk()
    player = carregar_jogo()
    if not player:
        player = Player(nome="Treinador")
    app = PokemonGUI(root, player)
    root.mainloop()

if __name__ == "__main__":
    main()
