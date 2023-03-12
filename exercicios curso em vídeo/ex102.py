def fatorial(n, show=False):
    """
    -> calcula o fatorial de um número
    :param n: numero que deseja ver o fatorial
    :param show: mostrar ou não o calculo
    :return: n fatorial
    -> criado por hiandalex
    """
    fator = 1
    for i in range(n, 0, -1):
        if show:
            print(i, " = " if i == 1 else "X", end=" ")
        fator *= i
    return fator


num = int(input("deseja ver o fatorial de qual número? "))
res = input("se deseja ver os calculos digite 1 "
            "se quer ver só o resultado digite 2: ")
while res not in "12":
    print("opção inválida")
    res = input("se deseja ver os calculos digite 1 "
                "se quer ver só o resultado digite 2:")
if res == "1":
    ver = True
else:
    ver = False
print(fatorial(num, ver))
