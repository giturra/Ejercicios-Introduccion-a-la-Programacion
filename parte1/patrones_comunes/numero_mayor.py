n = int(input("Ingrese n: "))
numeros = []
i = 0
while i < n:
    numeros.append(int(input("Ingrese número: ")))
    i += 1
max_num = numeros[0]
i = 1
while i < n:
    if max_num < numeros[i]:
        max_num = numeros[i]
    i += 1
print("El mayor es", max_num)