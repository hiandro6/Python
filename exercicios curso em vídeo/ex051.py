print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':=^30}")
print("=" * 30)
p1 = int(input("type the 1° term:"))
r = int(input("razão:"))
d = p1 + (10 - 1) * r
for i in range(p1, d + r, r):
    print(i, end=" -> ")
print("acabou")
