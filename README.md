🐉 Pokémon Battle – Projeto de Estudo de POO em Python

Interface gráfica em Tkinter + lógica de batalha + herança entre classes

<p align="center"> <img src="https://raw.githubusercontent.com/placeholder/Pokemon/thumb1.png" width="450"> </p>
🎯 Sobre o Projeto

Este projeto foi criado com o objetivo principal de praticar Programação Orientada a Objetos (POO) em Python, usando um mini-jogo inspirado no universo Pokémon.

Aqui você encontrará:

✔️ Herança (classe Pai → classes Filhas)

✔️ Polimorfismo (cada tipo de Pokémon ataca de forma diferente)

✔️ Composição (jogador possui pokémons, batalha usa objetos player + inimigo)

✔️ Tkinter para interface gráfica

✔️ Sistema de batalha por turnos

✔️ Escolha de Pokémon antes da luta

✔️ Level up automático a cada 3 vitórias

O jogo não tenta copiar Pokémon oficial — ele foca em ensinar e demonstrar POO de forma prática e divertida.

🧠 Objetivo de Aprendizado (POO)

O projeto foi idealizado para treinar os pilares da POO:

🔹 Herança
Pokemon (classe base)
├── PokemonFogo
├── PokemonAgua
└── PokemonEletrico

Pessoa
├── Player
└── Inimigo

🔹 Polimorfismo

Cada tipo de Pokémon possui seu método atacar() com lógica própria.

🔹 Encapsulamento

Cada classe controla seus próprios atributos como nível, HP e dano.

🔹 Composição

Players possuem lista de Pokémons, inimigos são gerados dinamicamente por nível.

📂 Estrutura do Projeto
📦 PokemonBattle/
 ┣ 📜 main.py
 ┣ 📜 gui.py
 ┣ 📜 pessoa.py
 ┣ 📜 pokemons.py
 ┣ 📜 batalha.py
 ┣ 📜 save_load.py
 ┣ 📁 assets/        (imagens opcionais)
 ┗ 📜 README.md

🚀 Como Rodar
1️⃣ Clonar o repositório
git clone https://github.com/SEU_USUARIO/PokemonBattle.git
cd PokemonBattle

2️⃣ Criar ambiente virtual (opcional)
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Instalar dependências

Tkinter já vem no Python padrão.

4️⃣ Executar o jogo
python3 main.py

🎮 Como Jogar
🧍‍♂️ No menu você pode:

Explorar — encontra um inimigo do mesmo nível

Ver Pokémons capturados

Salvar jogo

Sair

⚔️ Na batalha:

Escolha qual Pokémon quer usar

Ataque turno a turno

20% de chance de Golpe Especial

Barras de HP atualizam a cada golpe

Se vencer 3 batalhas → seu player sobe de nível

Seu Pokémon usado também sobe de nível a cada 3 vitórias

📈 Roadmap (futuras melhorias)

 Animações de ataque

 Sons (com pygame)

 Tela de escolha inicial mais bonita

 Sistema de tipos mais completo (fogo > planta, água > fogo etc.)

 Sprites reais dos Pokémon

 Inventário (poções, cura, escudo)

👨‍💻 Tecnologias Utilizadas

Python 3

Tkinter (GUI)

Programação Orientada a Objetos

Estrutura modular de classes

🙋‍♂️ Autor

Gabriel Palhano Gomes
Desenvolvedor em formação, com foco em Python, segurança, automação e boas práticas de código.
