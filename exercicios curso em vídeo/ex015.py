km = float(input("digite quantos km você percorreu:"))
dias = float(input("digite quantos dias você utilizou o carro:"))
valor_dia = 60 * dias
valor_km = 0.15 * km
price = valor_dia + valor_km
print(f"você percorreu {km} com o carro e o utilizou por {dias} o valor total a pagar é {price:.2f}R$")
