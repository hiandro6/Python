""""cat_oposto = float(input("digite o comprimento do cateto oposto:"))
cat_adje = float(input("digite o comprimento do cateto adjescente:"))
hipotenusa = ((cat_oposto**2)+(cat_adje**2))**(1/2)
print(f"sla pae só sei que fiz {hipotenusa:.2f}")"""
from math import hypot
co = float(input("digite o cateto oposto:"))
ca = float(input("digite o cateto adjescente:"))
hi = hypot(ca,co)
print(f"a hipotenusa vai medir {hi:.2f}")