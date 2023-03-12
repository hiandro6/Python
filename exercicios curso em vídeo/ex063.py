print("-" * 20)
print("sequência de fibonacci")
print("-" * 20)
termos = int(input("quantos termos você quer ver?"))
'''seque = 1
anterior = 0
anterior2 = 0
for i in range(1, termos + 1):
    if i % 2 == 0:
        anterior = seque
    else:
        anterior2 = seque
    seque = anterior + anterior2
    print(seque, end="-> ")'''
primeirot = 0
segundot = 1
terceirot = primeirot + segundot
print(f"{primeirot} > {segundot} > ", end="")
for i in range(3, termos + 1):
    terceirot = primeirot + segundot
    print(terceirot, end=" > ")
    primeirot = segundot
    segundot = terceirot
print("FIM")