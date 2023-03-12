soma = cont = 0
while True:
    num = int(input("type a number[999 to stop]: "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"the sum of the {cont} values is {soma}")
