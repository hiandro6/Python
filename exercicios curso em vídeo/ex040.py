n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota:"))
me = (n1 + n2) / 2
print(f"a média do aluno foi {me}")
if me >= 7:
    print("\033[1;32m aluno APROVADO\033[m")
elif me < 7 and me >= 5:
    print("tá de \033[;33mRECUPERAÇÃO\033[m man, vamo estudar mais aí né")
else:
    print("\033[4;31mREPROVADO\033[m ,chora aí bobão")
