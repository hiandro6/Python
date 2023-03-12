vel = float(input("a que velocidade está o seu carro?"))
if vel <= 80:
    print("ok,dentro do limite")
else:
    multa = (vel-80)*7
    print(f"acima do limite bro,vai ter que pagar uma multa de {multa} R$ ")