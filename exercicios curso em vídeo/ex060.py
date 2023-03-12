"""num = int(input("digite o número que deseja ver o calculo fatorial:"))
contador = num
fatorial = 1
while contador > 0:
    print(f"{contador}", end=" ")
    print("X " if contador > 1 else "=", end= "")
    fatorial = fatorial * contador
    contador = contador - 1
print(f" o fatorial é {fatorial}")"""
num = int(input("digite o número que deseja ver o calculo fatorial:"))
fat = 1
for i in range(num, 0, -1):
    print(i, end=" ")
    print("X" if i > 1 else "=", end=" ")
    fat = fat * i
print(fat)