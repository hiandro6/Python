from random import randint
print("""\033[32mparabéns você está participando do jogo da advinhação.\033[m
pensei em um número entre 0 e 10,consegue advinhar qual foi?""")
n = randint(1, 10)
c = int(input("qual seu palpite?"))
tentativas = 1
while c != n:
    tentativas += 1
    if n > c:
        c = int(input("mais...tente novamente:"))
    else:
        c = int(input("menos...tente novamente:"))
print(f"acertou com {tentativas} tentativas, \033[34mPARABÉNS\033[m")