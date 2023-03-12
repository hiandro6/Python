ex = input("digite sua expressão: ")
pilha = []
for i in ex:
    if i == "(":
        pilha.append("(")
    elif i == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("expressão válida")
else:
    print("expressão inválida")