from datetime import date
di = dict()
di['nome'] = input("nome: ")
atual = date.today().year
age = int(input("ano de nascimento: "))
di["idade"] = atual - age
di["cpts"] = int(input("carteira de trabalho [0 se você não tem]: "))
if di["cpts"] != 0:
    di["contratação"] = int(input("ano de contratação: "))
    di["salário"] = float(input("salário: R$"))
    di["aposentadoria"] = di["idade"] + ((di["contratação"] + 35) - atual)
print("~~"*20)
for k, v in di.items():
    print(f"{k} = {v}")