🎮 Pokémon em Python com Tkinter

Projeto desenvolvido para estudar Programação Orientada a Objetos (POO) utilizando Python e Tkinter — com foco em herança, polimorfismo, organização modular e um sistema simples de exploração + batalhas por turnos.

🔗 Repositório:
https://github.com/Gabrielpalhanogomes2803/Pok-mon-em-Python-com-Tkinter.git

📌 Sobre o Projeto

Este projeto recria um pequeno sistema inspirado em Pokémon para demonstrar, na prática:

Herança entre classes

Classes pai e subclasses

Polimorfismo com métodos sobrescritos

Separação de responsabilidades entre módulos

Estrutura de jogo com player, exploração e batalhas

Interface gráfica com Tkinter

O objetivo não é fazer um jogo completo, mas sim mostrar conceitos de POO funcionando de forma clara e organizada.

🧱 Estrutura do Projeto
📦 Pokemon-em-Python-com-Tkinter
│
├── main.py               # Início do jogo
├── gui.py                # Interface Tkinter
├── batalha.py            # Mecânica da batalha por turnos
├── Player.py             # Classe do jogador
├── Pokemon.py            # Classe base dos Pokémons
├── pokemons_tipos.py     # Subclasses dos tipos (fogo, água, planta)
├── utils.py              # Funções auxiliares
└── save_load.py          # Base futura para salvar/carregar progresso

🎮 Funcionalidades do Jogo
🧍 Escolha do Pokémon inicial

Antes de começar, o jogador escolhe qual Pokémon deseja usar.

🌿 Exploração

O jogador clica no botão Explorar, e um Pokémon inimigo aleatório do mesmo nível aparece para batalhar.

⚔️ Sistema de Batalha por Turnos

Ataque do jogador

Ataque do inimigo

HP recarregado no início do duelo

Vence quem zerar o HP adversário primeiro

📈 Sistema de Nível

O player ganha nível a cada vitória

O Pokémon usado ganha nível a cada 3 vitórias

O Pokémon inimigo sempre tem o mesmo nível do jogador

🪟 Interface gráfica com Tkinter

Simples e funcional, com:

Tela de escolha de Pokémon

Menu principal

Tela de exploração

Tela de batalha com resumo dos ataques

🧠 Objetivo Educacional (POO)

O projeto foca intensamente em:

✔️ Herança
class PokemonDeFogo(Pokemon):
    ...

✔️ Polimorfismo

Cada tipo tem ataque diferente.

✔️ Estados e atributos independentes

HP, nível, força, vitórias, etc.

✔️ Modularização

Arquivos separados e organizados.

✔️ Interação entre objetos

Player → Pokémon → Batalha

▶️ Como Executar
1. Clone o repositório
git clone https://github.com/Gabrielpalhanogomes2803/Pok-mon-em-Python-com-Tkinter.git

2. Entre no diretório
cd Pok-mon-em-Python-com-Tkinter

3. Execute o jogo
python3 main.py

🛠️ Tecnologias Utilizadas

Python 3

Tkinter (interface gráfica)

Estruturas de POO

Sistema modular em múltiplos arquivos

🚀 Futuras Melhorias

Sistema de captura

Vantagens de tipos (fogo > planta > água > fogo)

Tela inicial com menu animado

Sons e pequenas animações

Salvar e carregar progresso (save file)

Tela de status do Pokémon
