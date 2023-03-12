a = int(input("digite um número:"))
b = int(input("digite outro número:"))
c = int(input("digite mais um número:"))
d = int(input("digite o último número:"))
np = 0
t = (a, b, c, d)
for i in t:
    if i % 2 == 0:
        np += 1
print(f'o valor 9 apareceu {t.count(9)} vezes')
print(f'o valor 3 apareceu na posição {t.index(3) + 1}'if 3 in t else 'você não digitou o número 3')
print(f'você digitou {np} números pares')