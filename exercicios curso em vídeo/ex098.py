from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * (-1)
    if passo == 0:
        passo = 1
    print("-=" * 20)
    print(f"contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ")
            sleep(0.25)
        print("FIM")
    elif inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=" ")
            sleep(0.25)
        print("FIM")
    print("-="*20)


contador(1, 10, 1)
contador(10, 0, 2)
print("agora é a sua vez de personalizar a contagem!")
ini = int(input("Inicio: "))
fi = int(input("fim: "))
pas = int(input("passo: "))
contador(ini, fi, pas)
