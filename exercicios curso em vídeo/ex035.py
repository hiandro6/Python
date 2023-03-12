print("-=-"*20)
print("ANALISADOR DE TRIÂNGULOS")
print("=-="*20)
s1 = float(input("primeiro segmento:"))
s2 = float(input("segundo segmento:"))
s3 = float(input("terceiro segmento:"))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("podem formar um triângulo")
else:
    print("não podem formar um triângulo")