result = 0
while True:
    n = int(input("choose a number to see on the multiplication table: "))
    if n < 0:
        break
    for i in range(1, 11):
        result = n * i
        print(f"{n} X {i:2} = {result}")
    print("\033[34m~~\033[m"*30)
print("\033[33mthat's all folks!\033[m")
