print("_"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("_"*40)
t = ('lápis', 3.00, 'caderno', 40.00, 'mochila', 159.99)
for i in range(0, len(t)):
    # print(f"{t[i]:.<40}{'R$'}{t[i + 1]:>8}")
    if i % 2 == 0:
        print(f"{t[i]:.<30}", end="")
    else:
        print(f"R${t[i]:>7.2f}")
print("_"*40)
