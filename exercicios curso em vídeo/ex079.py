li = []
while True:
    v = (int(input("digite um valor:")))
    if v in li:
        print("valor duplicado, não vou adicionar...")
    else:
        li.append(v)
    r = input("quer continuar? [S/N]: ").lower().strip()[0]
    if r == "n":
        break
li.sort()
print(f"você digitou os valores: {li}")
