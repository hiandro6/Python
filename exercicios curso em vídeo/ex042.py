n1 = float(input("primeiro segmento:"))
n2 = float(input("2° segmento:"))
n3 = float(input("3° segmento:"))
if n1 + n2 > n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 and n1 == n3:
        print("podem formar um triângulo equilátero")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("podem formar um trângulo isósceles")
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print("podem formar um triângulo escaleno")
else:
    print("\033[1;31mNÃO PODEM FORMAR UM TRIÂNGULO!\033[m")
