v1 = int(input("primeiro valor:"))
v2 = int(input("segundo valor:"))
op = ""
while op != "5":
    print("\033[1;34m=-=\033[m" * 10)
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    op = input("qual sua opção?")
    soma = v1 + v2
    produto = v1 * v2
    maior = 0
    if op == "1":
        print(f"\033[35ma soma dos valores é \033[m{soma}")
    elif op == "2":
        print(f"\033[36mo produto dos valores é \033[m{produto}")
    elif op == "3":
        if v1 > v2:
            print(f"\033[37mo maior número é o \033[m{v1}")
        elif v2 > v1:
            print(f"\033[33mo maior número é o\033[m {v2}")
        else:
            print("\033[31mos dois valores são iguais\033[m")
    elif op == "4":
        v1 = int(input("primeiro valor:"))
        v2 = int(input("segundo valor:"))
    elif op != "1" and op != "2" and op != "3" and op != "4" and op != "5":
        print("\033[4;31mOPÇÃO INVÁLIDA!\033[m")