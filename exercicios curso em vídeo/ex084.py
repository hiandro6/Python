dados = []
li = []
mai = 0
men = 0
while True:
    dados.append(input("nome: "))
    dados.append(float(input("peso: ")))
    if len(li) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    li.append(dados[:])
    dados.clear()
    r = input("quer continuar? [S/N]: ").lower().strip()[0]
    while r != "s" and r != "n":
        print("\033[4;31mresposta invalida!\033[m")
        r = input("quer continuar? [S/N]: ").lower().strip()[0]
    if r == "n":
        break
print("-=-"*20)
print(f"você leu os dados de {len(li)} pessoas")
print(f"o maior peso foi o de {mai}kg. Peso de: ", end=" ")
for j in li:
    if j[1] == mai:
        print(f'[{j[0]}]')
print(f"\no menor peso foi o de {men}kg. Peso de:", end=" ")
for j in li:
    if j[1] == men:
        print(f'[{j[0]}]')