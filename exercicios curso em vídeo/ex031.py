km = float(input("qual a distância da sua viagem?"))
if km > 200:
    price = km*0.45
else:
    price = km*0.50
print(f"o valor da sua passagem é de {price},boa viagem!")