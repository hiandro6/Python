from random import randint
# n = tuple(sample(range(10), 5))
# n = [randint(0, 10) for i in range(5)]
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(n)
print(f'''o maior valor sorteado foi {sorted(n)[-1]}
o menor valor sorteado foi {sorted(n)[0]}''')
