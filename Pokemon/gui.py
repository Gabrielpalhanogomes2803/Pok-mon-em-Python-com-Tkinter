import tkinter as tk
from tkinter import messagebox
from pessoa import Player, Inimigo
from save_load import salvar_jogo
from Pokemon import *
import random

class PokemonGUI:
    def __init__(self, root, player):
        self.root = root
        self.player = player
        self.root.title("Pokémon Tkinter")
        self.root.geometry("500x500")

        if not self.player.pokemons:
            self.selecao_inicial_pokemons()
        else:
            self.menu_principal()

    def selecao_inicial_pokemons(self):
        for w in self.root.winfo_children():
            w.destroy()
        tk.Label(self.root, text="Escolha 3 Pokémons iniciais:", font=("Arial", 16)).pack(pady=20)

        pokemons_disponiveis = [
            PokemonEletrico("Pikachu"),
            PokemonDeFogo("Charmander"),
            PokemonDeAgua("Squirtle"),
            PokemonEletrico("Raichu"),
            PokemonDeFogo("Vulpix"),
            PokemonDeAgua("Poliwag")
        ]

        self.selecionados = []

        def toggle_pokemon(p):
            if p in self.selecionados:
                self.selecionados.remove(p)
            elif len(self.selecionados) < 3:
                self.selecionados.append(p)
            lbl.config(text="Selecionados: " + ", ".join(str(p) for p in self.selecionados))

        for p in pokemons_disponiveis:
            tk.Button(self.root, text=str(p), command=lambda pk=p: toggle_pokemon(pk)).pack(pady=2)

        lbl = tk.Label(self.root, text="Selecionados: ")
        lbl.pack(pady=5)

        def confirmar():
            if len(self.selecionados) != 3:
                messagebox.showwarning("Atenção", "Selecione exatamente 3 Pokémons!")
                return
            self.player.pokemons = self.selecionados
            self.menu_principal()

        tk.Button(self.root, text="Confirmar Escolha", command=confirmar).pack(pady=10)

    def menu_principal(self):
        for w in self.root.winfo_children():
            w.destroy()
        tk.Label(self.root, text=f"Bem-vindo, {self.player.nome}!", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Explorar", width=20, command=self.explorar_gui).pack(pady=10)
        tk.Button(self.root, text="Ver Pokémons", width=20, command=self.ver_pokemons).pack(pady=10)
        tk.Button(self.root, text="Salvar Jogo", width=20, command=self.salvar).pack(pady=10)
        tk.Button(self.root, text="Sair", width=20, command=self.root.quit).pack(pady=10)

    def explorar_gui(self):
        inimigo = Inimigo(player_level=self.player.nivel)
        messagebox.showinfo("Exploração", f"Um {inimigo.pokemons[0]} apareceu!")
        for w in self.root.winfo_children():
            w.destroy()
        BatalhaGUI(self.root, self.player, inimigo, self.menu_principal)

    def ver_pokemons(self):
        janela = tk.Toplevel(self.root)
        janela.title("Seus Pokémons")
        tk.Label(janela, text="Seus Pokémons:", font=("Arial", 14)).pack(pady=10)
        for p in self.player.pokemons:
            tk.Label(janela, text=f"{p} - Level {p.level}").pack()

    def salvar(self):
        salvar_jogo(self.player)
        messagebox.showinfo("Salvar", "Jogo salvo com sucesso!")

# ---------------- BATALHA ----------------
class BatalhaGUI:
    def __init__(self, root, player, inimigo, finalizar_callback):
        self.root = root
        self.player = player
        self.inimigo = inimigo
        self.finalizar_callback = finalizar_callback

        self.pokemon_player = None
        self.pokemon_inimigo = inimigo.pokemons[0]

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text=f"Inimigo: {self.pokemon_inimigo}").pack(pady=5)
        self.hp_canvas_inimigo = tk.Canvas(self.frame, width=200, height=20, bg="red")
        self.hp_canvas_inimigo.pack(pady=5)

        tk.Label(self.frame, text="Escolha seu Pokémon:").pack(pady=5)
        self.var_pokemon = tk.StringVar()
        self.var_pokemon.set("")

        for p in self.player.pokemons:
            tk.Radiobutton(self.frame, text=f"{p}", variable=self.var_pokemon, value=str(p)).pack(anchor='w')

        tk.Button(self.frame, text="Confirmar", command=self.confirmar_pokemon).pack(pady=5)

        self.btn_atacar = tk.Button(self.frame, text="Atacar", command=self.atacar, state='disabled')
        self.btn_atacar.pack(pady=10)
        self.btn_desistir = tk.Button(self.frame, text="Desistir", command=self.desistir, state='disabled')
        self.btn_desistir.pack(pady=5)

    def confirmar_pokemon(self):
        for p in self.player.pokemons:
            if str(p) == self.var_pokemon.get():
                self.pokemon_player = p
                break
        if not self.pokemon_player:
            messagebox.showwarning("Atenção", "Escolha um Pokémon!")
            return

        self.pokemon_player.hp = self.pokemon_player.level * 10
        self.pokemon_inimigo.hp = self.pokemon_inimigo.level * 10

        messagebox.showinfo("Batalha", f"Você escolheu {self.pokemon_player}!")
        self.btn_atacar.config(state='normal')
        self.btn_desistir.config(state='normal')

        tk.Label(self.frame, text=f"Seu Pokémon: {self.pokemon_player}").pack(pady=5)
        self.hp_canvas_player = tk.Canvas(self.frame, width=200, height=20, bg="red")
        self.hp_canvas_player.pack(pady=5)

        self.atualizar_hp()

    def atualizar_hp(self):
        if self.pokemon_player:
            hp_percent = max(0, self.pokemon_player.hp / (self.pokemon_player.level * 10))
            self.hp_canvas_player.delete("all")
            self.hp_canvas_player.create_rectangle(0,0,200*hp_percent,20,fill="green")
        hp_percent = max(0, self.pokemon_inimigo.hp / (self.pokemon_inimigo.level*10))
        self.hp_canvas_inimigo.delete("all")
        self.hp_canvas_inimigo.create_rectangle(0,0,200*hp_percent,20,fill="red")

    def atacar(self):
        dano = self.pokemon_player.atacar(self.pokemon_inimigo)
        if random.randint(1,5) == 1:
            dano_extra = self.pokemon_player.atacar(self.pokemon_inimigo)
            messagebox.showinfo("Golpe Especial!", f"{self.pokemon_player} causou {dano_extra} extra!")
        self.atualizar_hp()

        if self.pokemon_inimigo.hp <= 0:
            messagebox.showinfo("Vitória!", f"{self.pokemon_inimigo} desmaiou! Você venceu!")
            self.player.capturar(self.pokemon_inimigo)
            self.player.aumentar_vitorias()
            self.frame.destroy()
            self.finalizar_callback()
            return

        dano_inimigo = self.pokemon_inimigo.atacar(self.pokemon_player)
        self.atualizar_hp()

        if self.pokemon_player.hp <= 0:
            messagebox.showwarning("Derrota!", f"{self.pokemon_player} desmaiou! Você perdeu!")
            self.frame.destroy()
            self.finalizar_callback()
            return

    def desistir(self):
        if messagebox.askyesno("Desistir", "Deseja desistir da batalha?"):
            messagebox.showinfo("Batalha", "Você desistiu!")
            self.frame.destroy()
            self.finalizar_callback()
