def vota(nas):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - nas
    if idade >= 18 and idade <= 65:
        voto = f"com {idade} anos - VOTO OBRIGATÓRIO"
    elif idade >= 16 and idade < 18:
        voto = f"com {idade} anos - VOTO OPCIONAL"
    elif idade > 65:
        voto = f"com {idade} anos - VOTO OPCIONAL"
    else:
        voto = f"com {idade} anos - NÃO VOTA"
    return voto


nascimento = int(input("em que ano você nasceu? "))
print(vota(nascimento))