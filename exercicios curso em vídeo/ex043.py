p = float(input("digite o seu peso:"))
a = float(input("digite a sua altura"))
imc = p / (a**2)
print(f"o seu imc é de {imc}",end=' ')
if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("peso ideal")
elif imc >= 25 and imc < 30:
    print("sobrepeso")
elif imc >= 30 and imc < 40 :
    print("obesidade")
else:
    print("obesidade morbida")