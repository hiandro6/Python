n1 = float(input("digite o primeiro valor:"))
n2 = float(input("digite o segundo valor:"))
if n1 > n2:
    print(f"\033[1;36m{n1} é o maior")
elif n2 > n1:
    print(f"\033[1;33m{n2} é o maior")
else:
    print("\033[4;31mos dois números são iguais")