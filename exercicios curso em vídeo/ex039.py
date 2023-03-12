from datetime import date
ano = date.today().year
nas = int(input("em que ano você nasceu?"))
sex = input("digite o seu sexo M para masculino e F para feminino:").strip().upper
age = ano - nas
print(f"\033[1;34m quem nasceu em {nas} tem {age} anos em {ano}\033[m")
if sex == "M":
    if age == 18:
        print("\033[1;33m você tem que se alistar imediatamente!!!\033[m")
    elif age > 18:
        print(f"\033[1;31m você devia ter se alistado a {age - 18} ano(s) atrás\033[m")
        print(f"o ano do seu alistamento foi {nas + 18}")
    else:
        print(f"\033[1;32m seu alistamento será em {18 - age} ano(s)\033[m")
        print(f"o ano do seu alistamento será {nas + 18}")
else:
    print("o alistamento militar não é obrigatório para você,sortuda.")
