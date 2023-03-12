n = int(input("type a number:"))
vez = 0
for i in range(1, n+1):
    if n % i == 0:
        vez = vez + 1
        print(f"\033[1;32m{i}\033[m", end=" ")
    else:
        print(f"\033[1;31m{i}\033[m", end=" ")
if vez > 2:
    print(f"\no número {n} foi divisivel {vez} vezes,portanto não é primo")
else:
    print(f"\n o número {n} foi divisivel {vez} vezes, ele é primo")
