from random import randint
rank = {}
for i in range(1, 5):
    jo = randint(1, 6)
    rank[f"JOGADOR {i}"] = jo
for k, v in rank.items():
    print(f"o {k} tirou {v} no dado")
print("~~"*20)
print("  ==RANKING DOS JOGADORES==")
c = 1
for j in sorted(rank, key=rank.get, reverse=True):
    print(f"{c}° LUGAR = {j}, com {rank[j]} pontos")
    c += 1
print("zap")