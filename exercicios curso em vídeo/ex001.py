somav = 0
posi = 0
nega = 0
med = 0
perpo = 0
perne = 0
c = int(input("quantos valores deseja ler?"))
for i in range(1, c + 1):
    v = int(input(f"digite o {i}° valor:"))
    somav += v
    med = somav / c
    if v > 0:
        posi = posi + 1
        perpo = posi * 100 / c
    else:
        nega = nega + 1
        perne = nega * 100 / c
print(f"a média dos {c} valores é de {med} ,desses {posi} são positivos e {nega} são negativos")
print(f"{perpo}% positivos e {perne}% negativos")