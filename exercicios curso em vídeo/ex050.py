s = 0
c = 0
for i in range(1, 7):
    n = int(input(f"type the {i}° number:"))
    if n % 2 == 0:
        s = s + n
        c = c + 1
print(f"a soma dos {c}values pares foi {s}")
