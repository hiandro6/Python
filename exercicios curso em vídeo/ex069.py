p18 = h = m20 = 0
while True:
    print("-" * 30)
    print("CADASTRE UM PESSOA")
    print("-"*30)
    age = int(input("idade: "))
    sex = input("sexo [M/F]: ").lower().strip()[0]
    c = input("quer continuar? [S/N]: ")
    if age > 18:
        p18 += 1
    if sex == "m":
        h +=1
    if age < 20 and sex == "f":
        m20 +=1
    if c == "n":
        break
print(f'''pessoas com mais de 18 anos: {p18}
quantidade de homens: {h}
mulheres com menos de 20 anos: {m20}''')