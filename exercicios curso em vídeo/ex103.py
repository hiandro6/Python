def ficha(nome="<desconhecido>", gols=0):
    return f"o jogador {nome} fez {gols} gols no campeonato"


n = input("digite o nome do jogador: ").strip()
g = input("quantidade de gols: ").strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == "":
    print(ficha(gols=g))
else:
    print(ficha(n, g))
