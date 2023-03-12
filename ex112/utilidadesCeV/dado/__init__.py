def leiadinheiro(txt):
    while True:
        entrada = str(input(txt).strip().replace(",", "."))
        if not entrada.replace(".", "", 1).isnumeric():
            print(f"\033[31m\"{entrada}\" é um preço inválido!\033[m")
        else:
            return float(entrada)