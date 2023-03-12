fr = input("type a phrase:").strip().upper()
sepa = fr.split()
junt = "".join(sepa)
inverso = ""
for i in range(len(junt) - 1, -1, -1):
    inverso = inverso + junt[i]
if inverso == junt:
    print(f"{fr} ao contrário é {inverso},formam um palindromo")
else:
    print(f"{fr} ao contrário é {inverso}, não forma um palindromo")