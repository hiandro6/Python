di = dict()
di["nome"] = input("nome: ")
di["media"] = float(input("media: "))
if di["media"] < 5:
    di["situação"] = "reprovado"
elif di["media"] < 7:
    di["situação"] = "recuperação"
else:
    di["situação"] = "aprovado"
print("_"*30)
for k, v in di.items():
    print(f"-{k} é igual a {v}")
