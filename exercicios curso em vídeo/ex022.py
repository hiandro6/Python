'''O nome com todas as letras maiúsculas e minúsculas.Quantas letras aotodo (sem considerar espaços)
Quantas letras tem o primeiro nome.'''
name = input("type your name mf:")
print(f"seu nome em maiusculas é {name.upper()}")
print(f"seu nome em minúsculas é {name.lower()}")
new = name.split()
newn = "".join(new)
print(f"seu nome tem no total {len(newn)} letras")
print(f"seu primeiro nome tem {len(new[0])} letras")
#print(f"seu nome tem {len(name)-name.count(' ')}letras")
#print(f"seu nome tem {len(name.replace(' ',''))} letras")