from random import randint
num = int(input("pense em um número:"))
numc = randint(0, 5)
print(f"o número sorteado foi {numc}")
if num == numc:
    print("acertou mizeravi")
else:
    print("você errou,tente novamente")