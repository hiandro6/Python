times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Curitiba', 'Avaí', 'Ponte preta', 'Atlético-GO')
print(f'''OS 5 PRIMEIROS TIMES SÃO: {times[0:5]}
OS 4 ULTIMOS SÃO: {times[-4:]}
TIMES EM ORDEM ALFABETICA: {sorted(times)}
o chapecoense está na {times.index("Chapecoense") + 1}° posição''')