print("gerador de PA")
print("=-=" * 10)
p1 = int(input("primeiro termo:"))
r = int(input("razão:"))
c = 0
pa = p1
while c < 10:
    print(f"{pa} > ", end=" ")
    pa = pa + r
    c = c + 1
print("pausa")
nc = 0
am = 1
while am != 0:
    am = int(input("quantos termos você quer mostrar a mais?"))
    nc = 0
    while nc < am:
        print(f"{pa} > ", end=" ")
        pa = pa + r
        nc = nc + 1
        c = c + 1
print(f"a quantidade de termos mostrada foi {c}")
