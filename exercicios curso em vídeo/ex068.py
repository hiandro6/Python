from random import randint
print("~~"*20)
print("\033[33mJOGO DO PAR OU ÍMPAR\033[m")
print("~~"*20)
qntv = 0
while True:
    jog = input("\033[34mPAR OU IMPAR?[P/I]\033[m ").strip().lower()[0]
    nj = int(input("escolha um valor de 0 a 10:"))
    np = randint(0, 10)
    soma = nj + np
    print(f"você escolheu \033[35m{nj}\033[m e o computador escolheu \033[35m{np}\033[m")
    print(f"a soma deu {soma}")
    print("PAR"if soma % 2 == 0 else "IMPAR")
    if soma % 2 == 0 and jog == "p":
        print("\033[32mVOCÊ VENCEU!\033[m")
        qntv += 1
    elif soma % 2 == 1 and jog == "i":
        print("\033[32mVOCÊ VENCEU!\033[m")
        qntv += 1
    elif soma % 2 == 0 and jog == "i":
        print("\033[31mVOCÊ PERDEU\033[m")
        break
    elif soma % 2 == 1 and jog == "p":
        print("\033[31mVOCÊ PERDEU\033[m")
        break
    print("\033[34m~~\033[m"*20)
print(f"quantidade de vitórias consecutivas: {qntv}")