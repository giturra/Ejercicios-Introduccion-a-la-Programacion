n = int(input("Ingrese el número: "))
i = 0
while i < n:
    if i % 3 != 0 and i % 7 != 0:
        print(i)
    i += 1