s = ('Python', 'Hacker', 'Pygame', 'Linux', 'Rico', 'Feliz', 'Casado', 'Desenvolvedor', 'Empresario', 'programador')
for i in s:
    print(f'\n\033[34mna palavra {i} temos\033[m', end=" ")
    '''for j in range(0, i.count('a')):
        print("a", end=" ")
    for j in range(0, i.count('e')):
        print("e", end=" ")
    for j in range(0, i.count('i')):
        print("i", end=" ")
    for j in range(0, i.count('o')):
        print("o", end=" ")
    for j in range(0, i.count('u')):
        print("u", end=" ")'''
    for j in i:
        if j.lower() in 'aeiou':
            print(j.lower(), end=" ")
print("\nfim")