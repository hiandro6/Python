s = 0
c = 0
for i in range(3, 501, 3):
    if i % 2 == 1:
        s = s + i
        c = c + 1
print(f"a soma entre os {c} valores é {s}")
