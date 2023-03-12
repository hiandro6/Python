n1 = float(input("digite o 1° valor:"))
n2 = float(input("digite o 2° valor:"))
n3 = float(input("digite o 3° valor:"))
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior valor")
elif n2 > n1 and n2 > n3:
    print(f"{n2}é o maior valor")
elif n3>n1 and n3 > n2:
    print(f"{n3} é o maior valor")
if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor valor")
elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor valor")
elif n3 < n1 and n3 < n2:
    print(f"{n3} é o menor valor")