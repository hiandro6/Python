from datetime import date
ano = date.today().year
ma = 0
me = 0
for i in range(1, 8):
    nas = int(input(f"digite o ano que a {i}° pessoa nasceu:"))
    if ano - nas >= 18:
        ma = ma + 1
    else:
        me = me + 1
print(f"{ma} pessoas são maiores de idade e {me} pessoas são menores de idade")