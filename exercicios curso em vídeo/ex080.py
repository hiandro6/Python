li = []
n = 0
for i in range(0, 5):
    n = int(input("digite um valor:"))
    if i == 0 or n > li[-1]:
        li.append(n)
        print("valor adicionado no final da lista...")
    else:
        pos = 0
        while pos < len(li):
            if n < li[pos]:
                li.insert(pos, n)
                print(f"valor adicionado na posição {pos}")
                break
            pos += 1
print(f"sua lista em ordem: {li}")