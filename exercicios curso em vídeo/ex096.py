def area(largura, comprimento):
    a = largura * comprimento
    print(f"a área de um terreno de {largura}X{comprimento} é de {a}m²")


l = float(input("LARGURA (m): "))
c = float(input("comprimento (m): "))
area(l, c)
