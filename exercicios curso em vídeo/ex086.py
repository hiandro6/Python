'''li = [[], [], []]
p = 0
pp = 0
for i in range(0, 9):
    if i == 3:
        p += 1
        pp = 0
    if i == 6:
        p += 1
        pp = 0
    li[p].append(int(input(f"digite um valor para a posição [{p}, {pp}]: ")))
    pp += 1
for i in li:
    print(f"[ {i[0]:^3} ] [ {i[1]:^3} ] [ {i[2]:^3} ]")'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"digite um valor para a posição [{i}, {j}]: "))
print("~~"*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()