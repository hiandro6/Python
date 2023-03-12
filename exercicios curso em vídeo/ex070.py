print("_"*30)
print(f"{'FUKUROU SUPERMERCADOS':^30}")
print(""*30)
tot = p1000 = menor = contador = 0
barato = ""
while True:
    contador += 1
    n = input("nome do produto: ")
    p = float(input("preço: "))
    c = input("quer continuar [S/N]:")[0]
    while c not in "SsNn":
        c = input("quer continuar [S/N]:")[0]
    tot += p
    if p > 1000:
        p1000 += 1
    if contador == 1 or p < menor:
        menor = p
        barato = n
    if c in "nN":
        break
print(f'''o total da compra foi R${tot:.2f}
foram comprados {p1000} produtos acima de R$ 1000
o produto mais barato foi {barato} que custou R${menor:.2f}''')
