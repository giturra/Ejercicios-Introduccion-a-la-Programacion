n = int(input("Ingrese n: "))

s1 = 0
i = 1
while i <= n:
    s1 += i
    i += 1

print("S1:", s1)

s2 = (n * (n + 1) / 2)

print("S2:", int(s2))
if s1 == s2:
    print("Son iguales")
else:
    print("No son iguales")
