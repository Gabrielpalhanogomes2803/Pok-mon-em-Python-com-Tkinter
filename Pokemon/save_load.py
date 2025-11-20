import pickle

def salvar_jogo(player):
    with open("save.pkl", "wb") as f:
        pickle.dump(player, f)

def carregar_jogo():
    try:
        with open("save.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return None

