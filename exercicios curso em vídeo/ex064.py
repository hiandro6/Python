soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input("digite um número \033[31m[999 pra parar]:\033[m "))
    if n != 999:
        soma += n
        cont += 1
print(f"\033[34ma soma dos {cont} valores foi {soma}\033[m")
