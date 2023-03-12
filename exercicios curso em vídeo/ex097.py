def escreva(txt):
    tam = len(txt) + 6
    print("~" * tam)
    print(f"{txt.center(tam)}")
    print("~" * tam)


escreva("zap")
