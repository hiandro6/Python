def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print("\033[31mERRO seu fudido\033[m")


na = leiaInt("digite um número: ")
print(f"você digitou o número {na}")