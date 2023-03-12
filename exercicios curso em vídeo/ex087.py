li = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        li[i].append(int(input(f"digite um valor para a posição [{i}, {j}]: ")))
print("~~"*25)
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{li[i][j]:^5}]", end="")
    print()
print("~~"*25)
vp = v3 = m2 = c = 0
for po, w in enumerate(li):
    for p, y in enumerate(w):
        if po == 1:  #verificando linha
            if c == 0 or y > m2:
                m2 = y
        if p == 2:  #verificando coluna
            v3 += y
        if y % 2 == 0:  #verificando cada elemento
            vp += y
        c += 1
print(f'''soma de todos os valores pares digitados: {vp}
soma dos valores da terceira coluna: {v3}
o maior valor da segunda linha é: {m2}''')
print("~~"*25)
