from time import sleep
from random import randint
li = []
a = []
print("="*30)
print(f"{'PALPITE MEGA SENA':^30}")
print("="*30)
sleep(0.5)
n = int(input("quantos jogos você quer que eu sorteie? "))
sleep(0.7)
print(f"SORTEANDO {n} JOGOS")
for i in range(1, n + 1):
    for j in range(1, 7):
        v = randint(1, 60)
        if v not in li:
            li.append(v)
        else:
            while True:
                v = randint(1, 60)
                if v not in li:
                    li.append(v)
                    break
    li.sort()
    a.append(li[:])
    sleep(0.7)
    print(f"jogo {i}: {li}")
    li.clear()
print("\033[32mBOA SORTE!\033[m")
