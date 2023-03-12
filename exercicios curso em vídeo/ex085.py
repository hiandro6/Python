'''li = []
p = []
im = []
for i in range(1, 8):
    li.append(int(input(f"digite o {i}° valor: ")))
for j in li:
    if j % 2 == 0:
        p.append(j)
    else:
        im.append(j)
p.sort()
im.sort()
print(f"""os pares são {p}
os impares são {im}""")'''
v = [[], []]
for i in range(1, 8):
    va = int(input(f"digite o {i}° valor: "))
    if va % 2 == 0:
        v[0].append(va)
    else:
        v[1].append(va)
v[0].sort()
v[1].sort()
print(f"""os pares são {v[0]}
os impares são {v[1]}""")