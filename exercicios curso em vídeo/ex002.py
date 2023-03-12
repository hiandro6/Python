'''price = input("digite o valor do produto comprado:")
preco = float(price)
desconto = preco*0.05
x = preco-desconto
print(f"o preço anterior era de {preco:.2f} com o desconto de 5% o novo valor é {x:.2f}")'''
from datetime import date
from time import sleep
print("ESSE PROGRAMA MOSTRA DATAS POR EXTENSO")
meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
while True:
    print("-="*20)
    print("""[1] MOSTRAR A DATA DE HOJE
[2] ESCREVER MINHA PRÓPRIA DATA
[3] FECHAR O PROGRAMA""")
    print("-=" * 20)
    opcao = input("digite sua opção: ")
    while opcao not in "123":
        print("OPÇÃO INVÁLIDA, DIGITE NOVAMENTE!")
        opcao = input("digite sua opção: ")
    if opcao == "1":
        atual_aux = date.today()
        atual = str(atual_aux).split("-")
        atual.reverse()
        mesatual = int(atual[1])
        print(f"{atual[0]} de {meses[mesatual]} de {atual[2]}")
    if opcao == "2":
        data = input("digite uma data: ").split("/")
        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            bissexto = "sim"
        else:
            bissexto = "não"
        while True:
            if dia <= 0 or dia >= 32 or mes <= 0 or mes >= 13:
                print("DATA INVÁLIDA, DIGITE NOVAMENTE!")
                data = input("digite uma data: ").split("/")
                dia = int(data[0])
                mes = int(data[1])
                ano = int(data[2])
                if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                    bissexto = "sim"
                else:
                    bissexto = "não"
            elif mes == 2 and dia >= 30:
                print("DATA INVÁLIDA,fevereiro não tem mais que 29 dias,DIGITE NOVAMENTE!")
                data = input("digite uma data: ").split("/")
                dia = int(data[0])
                mes = int(data[1])
                ano = int(data[2])
                if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                    bissexto = "sim"
                else:
                    bissexto = "não"
            elif bissexto == "não" and mes == 2 and dia >= 29:
                print("DATA INVÁLIDA,fevereiro só tem 29 dias em ano bissexto DIGITE NOVAMENTE!")
                data = input("digite uma data: ").split("/")
                dia = int(data[0])
                mes = int(data[1])
                ano = int(data[2])
                if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                    bissexto = "sim"
                else:
                    bissexto = "não"
            else:
                print(f"{dia} de {meses[mes]} de {ano}")
                break
    if opcao == "3":
        print("FINALIZANDO...")
        sleep(1)
        break
print("tenha um ótimo dia !")
