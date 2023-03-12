print("\033[4;35m será que você pode financiar essa casa?\033[m")
print("=-=" * 15)
vc = float(input("digite o valor da casa:"))
sa = float(input("digite o valor do seu salário:"))
ano = int(input("digite em quantos anos você quer pagar:"))
p = (vc/ano)/12
if p > (sa * 30/100):
    print(f"para financiar uma casa de {vc} as parcelas seriam de R${p:.2f},\033[1;31mEMPRESTIMO NEGADO")
else:
    print(f"\033[1;32memprestimo aprovado\033[m suas parcelas serão de R${p:.2f} mensais durante {ano} anos", end=' ')
print("tenha um ótimo dia seu pobre")