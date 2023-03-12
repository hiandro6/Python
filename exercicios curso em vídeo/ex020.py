import random
al1 = input("digite o nome da primeira pessoa:")
al2 = input("digite o nome da segunda pessoa:")
al3 = input("digite o nome da terceira pessoa:")
al4 = input("digite o nome da quarta pesssoa:")
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(f"a ordem de apresentação será {lista}")