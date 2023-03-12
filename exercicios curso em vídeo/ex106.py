from time import sleep
c = {
    'padrao': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[0;30;107m'
}


def ajuda(com, cor="branco"):
    titulo(f"acessando o manual do comando \"{com}\"...", "roxo")
    print(c[cor], end="")
    help(com)
    print(c["padrao"])
    sleep(1.5)


def titulo(msg, cor="padrao"):
    tam = len(msg) + 6
    print("~" * tam)
    print(c[cor], end="")
    print(f"{msg.center(tam)}", end="")
    print(c["padrao"])
    print("~" * tam)
    sleep(1)


while True:
    titulo("SISTEMA DE AJUDA PyHELP", cor="verde")
    comando = input("função ou biblioteca> ").lower().strip()
    if comando == "fim":
        titulo("ATÉ LOGO !", "azul")
        break
    else:
        ajuda(comando, cor="branco")
