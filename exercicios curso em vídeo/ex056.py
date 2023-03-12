con = 0
soma = 0
hve = 0
mm2 = 0
for i in range (1, 5):
    print(f"{i}° PESSOA")
    n = input("nome:")
    id = int(input("idade:"))
    s = input("sexo(M/F):").lower()
    con = con + 1
    soma = soma + id
    if i == 1:
        hve = id
    else:
        if s == "m" and id > hve:
            hve = id
            nomedovei = n
    if s == "f" and id > 20:
        mm2 = mm2 +1
    if s == "m" and hve > id:
        print(n)
media = soma / con
print(f"o homem mais velho se chama {nomedovei} e tem {hve} anos")
print(f"a média de idade do grupo é de {media} anos")
print(f"ao todo são {mm2} mulheres com mais de 20 anos")