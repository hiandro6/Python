maior = 0
menor = 0
for i in range(1, 6):
    p = float(input(f"digite o peso da {i}° pessoa:"))
    if i == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f"o maior peso lido foi {maior}KG e o menor foi {menor}KG")