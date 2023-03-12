sal = float(input("informe o seu salário:"))
if sal <= 1250:
    new = sal * 15/100
    print(f"seu salário era de {sal} R$ com um aumento de 15% seu novo salário é {sal + new}R$")
else:
    new = sal * 10/100
    print(f"seu salário era de {sal}R$ com um aumento de 10% seu novo salário é {sal+new}")