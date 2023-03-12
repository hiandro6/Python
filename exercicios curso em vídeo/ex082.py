li = []
im = []
par = []
while True:
    v = int(input("digite um valor: "))
    li.append(v)
    if v % 2 == 0:
        par.append(v)
    else:
        im.append(v)
    r = input("quer continuar [S/N]: ").lower().strip()[0]
    while r != "n" and r != "s":
        print("resposta inválida")
        r = input("quer continuar [S/N]: ").lower().strip()[0]
    if r == "n":
        break
print(f'''a lista completa é {li}
a lista de números pares é {par}
a lista de impares é {im}''')