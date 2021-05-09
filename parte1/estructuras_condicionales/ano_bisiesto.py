anno = int(input("Ingrese un año: "))

cond = anno % 4 == 0

if cond:
    print(anno, "es bisiesto")
else:
    print(anno, "no es bisiesto")