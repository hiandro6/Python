def notas(*nota, sit=False, tab=False):
    """
        -> Função para analisar funções e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias).
        :param sit: opcional, indica se deve ou não adicionar a situação da turma.
        :param tab: opcional, indica se deve ou não mostrar os dados em forma de tabela.
        :return: dicionário e/ou tabela com os dados solicitados.
        """
    di = {}
    c = 0
    soma = 0
    for i in nota:
        c += 1
        soma += i
    media = soma / c
    di["total"] = c
    di["maior"] = max(nota)
    di["menor"] = min(nota)
    di["media"] = media
    if sit:
        if media > 6:
            di["situação"] = "BOA"
        else:
            di["situação"] = "RUIM"
    if tab:
        for k, v in di.items():
            print(f"{k:<10} = {v:^10}")
    if not tab:
        print(di)


num = []
qnt_notas = int(input("quantas notas deseja anexar? "))
for i in range(1, qnt_notas + 1):
    num.append(int(input(f"digite a {i}° nota: ")))
situation = input("deseja ver a situação? [S/N] ")[0].upper().strip()
tabela = input("deseja ver em formato de tabela? [S/N] ")[0].upper().strip()
if situation == 'S':
    if tabela == 'S':
        notas(*num, sit=True, tab=True)
    else:
        notas(*num, sit=True)
else:
    if tabela == 'S':
        notas(*num, tab=True)
    else:
        notas(*num)


