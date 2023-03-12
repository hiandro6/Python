'''a = []
mai = 0
men = 0
for i in range(0, 5):
    a.append(int(input(f"digite um valor para a posição {i}:")))
    if i == 0:
        mai = men = a[i]
    else:
        if a[i] > mai:
            mai = a[i]
        if a[i] < men:
            men = a[i]
print(f"você digitou os valores: {a}")
print(f"o maior número digitado foi {mai} e o menor foi {men}")
print("nas posições:", end=" ")
for p, j in enumerate(a):
    if j == mai:
        print(f"posição do maior{p}")
    if j == men:
        print(f"posição do menor: {p}")'''
val = []
for i in range(0, 5):
    val.append(int(input(f"digite o valor da posição {i}:")))
print(f"o maior valor foi {max(val)}, nas posições: ")
for p, j in enumerate(val):
    if j == max(val):
        print(f"{p}...", end=" ")
print(f"\no menor valor foi {min(val)}, nas posições:")
for p, j in enumerate(val):
    if j == min(val):
        print(f"{p}...", end=" ")