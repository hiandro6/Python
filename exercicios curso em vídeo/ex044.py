print(f"\033[1;34mFUKUROU SUPERMERCADOS\033[m")
price = float(input("type the price of your grocery:"))
print("""FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
fp = input("digite como deseja pagar:")
while True:
    if fp == "1":
        np = price - (price * 10/100)
    elif fp == "2":
        np = price - (price * 5/100)
    elif fp == "3":
        np = price
        print(f"sua compra será dividida em 2x de R${np/2}")
    elif fp == "4":
        pa = int(input("em quantas parcelas deseja dividir?"))
        np = (price + (price * 20/100))
        valp = np / pa
        print(f"sua compra será divida em {pa}x de R${valp:.2f}")
    else:
        while fp != "1" or "2" or "3" or "4":
            print("\033[1;31mOPÇÃO INVÁLIDA,TENTE NOVAMENTE!\033[m")
            fp = input("digite como deseja pagar:")
            if fp in "1234":
                break
        continue
    break
print(f"o valor da suas compras era de {price}R$ no final ficou de {np}R$ ")
