from math import radians, sin, cos, tan
ang = float(input("digite o valor do angulo:"))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print(f"o valor do seno é {seno:.2f}, o valor do cosseno é {coss:.2f} e o valor da tangente é {tang:.2f}")