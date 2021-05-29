n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
i = 0
resultado = 1
while i < m:
    resultado *= (n + i)
    print(i)
    i += 1

print(resultado)
print(n ** m)
