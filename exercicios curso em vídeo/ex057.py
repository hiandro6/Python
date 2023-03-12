from emoji import emojize
print(emojize("EITA BIXO,SEXO :fire:"))
s = input("digite o seu sexo [M/F]:").lower()
#while s not in "mMfF":
while s != "m" and s != "f":
    print(emojize("\033[31mDIGITOU ERRADO FDP\033[m:angry_face:"))
    s = input("digite novamente:").lower()
