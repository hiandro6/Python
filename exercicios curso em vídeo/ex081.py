li = []
while True:
    v = int(input("digite um valor: "))
    li.append(v)
    r = input("quer continuar? [S/N]: ").lower().strip()[0]
    if r == "n":
        break
print(f"você digitou {len(li)} valores")
if 5 in li:
    print("o valor 5 se encontra na lista.")
else:
    print("o valor 5 não pertence a lista")
li.sort(reverse=True)
print(f"a lista em ordem decrescente é {li}")