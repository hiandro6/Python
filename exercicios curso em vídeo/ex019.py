"""import random
al1 = input("digite o nome da primeira pessoa:")
al2 = input("digite o nome da segunda pessoa:")
al3 = input("digite o nome da terceira pessoa:")
al4 = input("digite o nome da quarta pesssoa:")
sor = random.randint(1,4)
if sor == 1:
    print(f"o sorteado foi {al1}")
elif sor == 2:
    print(f"o sorteado foi {al2}")
elif sor == 3:
    print(f"o sorteado foi {al3}")
else:
    print(f"o sorteado foi {al4}"""
from random import choice
al1 = input("digite o nome da primeira pessoa:")
al2 = input("digite o nome da segunda pessoa:")
al3 = input("digite o nome da terceira pessoa:")
al4 = input("digite o nome da quarta pesssoa:")
lista =[al1, al2, al3, al4]
escolhido = choice(lista)
print(f"o sorteado foi {escolhido}")