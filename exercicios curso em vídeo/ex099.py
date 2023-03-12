def maior(*n):
    print(f"analisando valores...{n}")
    print(f"foram {len(n)} valores ao todo")
    print(f"o maior valor é {max(n)}")


def maiorr(*nu):
    c = mai = 0
    print("analisando valores..")
    for i in nu:
        print(i, end=" ")
        if i > mai or c == 0:
            mai = i
        c +=1
    print(f"\nforam informados {c} valores, o maior valor é {mai}")
    print("-="*25)


maiorr(1, 2, 6, 3)
maiorr()