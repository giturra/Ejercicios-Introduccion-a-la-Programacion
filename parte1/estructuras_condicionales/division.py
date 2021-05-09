dividiendo = int(input("Dividiendo: "))
divisor = int(input("Divisor: "))

cond = dividiendo % divisor == 0

if cond:
    print("La división es exacta")
else:
    print("La división no es exacta")


print("Cociente:", int(dividiendo / divisor))
print("Resto:", dividiendo % divisor)