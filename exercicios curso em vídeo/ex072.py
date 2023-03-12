n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
     'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
op = "s"
while True:
    if op == "n":
        break
    while op != "s":
        print("opção inválida")
        op = input("quer continuar? [S/N]: ").strip().lower()[0]
    while True:
        nu = int(input("digite um  número de 0 a 20: "))
        if nu >= 0 and nu <=20:
            break
        print("TENTE NOVAMENTE")
    print(f"você digitou o número {n[nu]}")
    op = input("quer continuar? [S/N]: ").strip().lower()[0]
print("fim do programa")
# mes = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')