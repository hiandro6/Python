li = []
temp = []
while True:
    temp.append(input("nome: "))
    temp.append(float(input("nota 1: ")))
    temp.append(float(input("nota 2: ")))
    li.append(temp[:])
    temp.clear()
    r = input("quer conntinuar? [S/N]: ").lower().strip()[0]
    while r != "n" and r != "s":
        print("resposta invalida")
        r = input("quer conntinuar? [S/N]: ").lower().strip()[0]
    if r == "n":
        break
print("-="*30)
s = 0
me = 0
print(f"{'N°':<4}{'NOME':<20}{'MÉDIA':>5}")
for pp, i in enumerate(li):
    print(f"{pp:<4}{i[0]:<20}", end="")
    for p, j in enumerate(i):
        if p > 0:
            s += j
        if p == 2:
            me = s / 2
            print(f"{me:>5}")
            s = 0
while True:
    n = int(input("mostrar as notas de qual aluno? [999 interrompe]: "))
    if n == 999:
        print("finalizando...")
        break
    if n <= len(li) - 1:
        print(f"notas de {li[n][0]} são {li[n][1:]}")
print("<<<VOLTE SEMPRE>>>")