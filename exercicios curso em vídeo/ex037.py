num = int(input("digite um número inteiro qualquer:"))
print("=-="*20)
print("""escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
es = int(input("sua escolha:"))
if es == 1:
    print("{} convertido para binário fica {:b}".format(num, num))
elif es == 2:
    print("{} convertido para octal fica {:o}".format(num, num))
elif es == 3:
    print("{} convertido para hexadecimal fica {:x}".format(num, num))