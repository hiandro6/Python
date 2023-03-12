from random import randint
from time import sleep
print("""suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
j = input("qual é a sua jogada?")
if j == "0":
    pc = "PEDRA"
elif j == "1":
    pc = "PAPEL"
elif j == "2":
    pc = "TESOURA"
print("JO!")
sleep(1)
print("KEN!")
sleep(1)
print("PO!")
cj = str(randint(0,2))
if cj == "0":
    cc = "PEDRA"
elif cj == "1":
    cc = "PAPEL"
elif cj == "2":
    cc = "TESOURA"
#probabilidades empate
if cj == "0" and j == "0":
    print("EMPATE!")
elif cj == "1" and j == "1":
    print("EMPATE!")
elif cj == "2" and j == "2":
    print("EMPATE!")
#pcganhou
elif cj == "0" and j == "2" or cj == "1" and j == "0" or cj == "2" and j == "1":
    print("\033[1;31mo computador ganhou\033[m")
else:
    print("\033[1;32mo jogador ganhou\033[m")
print(f"o computador jogou {cc} e você jogou {pc}")
