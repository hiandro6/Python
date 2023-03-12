print("-"*30)
print(f"{'CAIXA ELETRONICO':^30}")
print("-"*30)
n50 = n20 = n10 = n1 = 0
v = int(input("quanto você deseja sacar?"))
while v >= 50:
    n50 += 1
    v = v - 50
while v >= 20:
    n20 += 1
    v -= 20
while v >= 10:
    n10 += 1
    v -= 10
while v >= 1:
    n1 += 1
    v -= 1
print(f'''{n50} cédulas de 50 reais
{n20} cédulas de 20 reais
{n10} cédulas de 10 reais
{n1} moedas de 1 real ''')
