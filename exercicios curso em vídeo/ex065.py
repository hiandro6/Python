maior = 0
menor = 0
media = 0
cont = 0
resp = "S"
while resp == "S":
    num = int(input("digite um número: "))
    cont = cont + 1
    media = media + num
    if cont == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input("quer continuar?[S/N]: ").upper().strip()[0]
mediaf = media / cont
print(f"a média dos {cont} números digitados foi {mediaf}")
print(f"o maior número foi {maior} e o menor foi {menor}")